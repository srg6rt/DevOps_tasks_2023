#from django.shortcuts import render
#from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
import pandas as pd
#from django.conf import settings

from .forms import URLForm
import re # for remove <br> tags from comments
TAG_RE = re.compile(r'<[^>]+>')
#from apiclient.discovery import build
from googleapiclient.discovery import build
from .models import Comments
from django.views.generic import ListView
import json
from urllib.request import urlopen

#url_for_compare = '' # Need variable for first run server

#
def index(request):
    return render(request, 'frontpage/index.html')


def get_youtube_url(request):
    global url_for_compare
    global api_for_compare
    global service
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = URLForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            
            url_for_compare = request.POST.get('paste_youtube_url')
            api_for_compare = request.POST.get('paste_youtube_api')
            print(api_for_compare)
            service = build('youtube', 'v3', developerKey=api_for_compare)
            check_url_for_exist_in_database(url_for_compare, api_for_compare)
            
            # redirect to a new URL:
            return render(request, 'frontpage/video_data_info.html', {'url_for_compare': url_for_compare})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = URLForm()

    return render(request, 'frontpage/video_data_info.html', {'form': form})


api_key = ''
keys =iter([])


def remove_tags(text):

    return TAG_RE.sub('', text)


def get_video_comments_1(service, **kwargs):

    separator = "\t__\t"
    comments = []
    number_of_replies = []
    results = service.commentThreads().list(**kwargs).execute()
    
    while results:
        for item in results['items']:
            one_comment = []
            id_comment =  item['id']
            user_name = item['snippet']['topLevelComment']['snippet']['authorDisplayName']
            comment = remove_tags(item['snippet']['topLevelComment']['snippet']['textDisplay'].replace('\r', ''))
            youtube_channel = item['snippet']['topLevelComment']['snippet']['authorChannelUrl']
            publishedAt = item['snippet']['topLevelComment']['snippet']['publishedAt']
            updatedAt = item['snippet']['topLevelComment']['snippet']['updatedAt']
            totalReplyCoun = item['snippet']['totalReplyCount']
                       
            one_comment.append(id_comment)
            one_comment.append(youtube_channel)
            one_comment.append(user_name)
            one_comment.append(publishedAt)
            one_comment.append(updatedAt) 
            one_comment.append(comment)
            
            comments.append(one_comment)
            
            totalReplyCoun = item['snippet']['totalReplyCount']
            if totalReplyCoun > 0:
                #print(totalReplyCoun)
                number_of_replies.append(id_comment)
        if 'nextPageToken' in results:
            kwargs['pageToken'] = results['nextPageToken']
            results = service.commentThreads().list(**kwargs).execute()
        else:
            break
    return comments, number_of_replies


def get_comments_from_comment(service, **kwargs):

    separator = "\t__\t"
    comments = []
    results = service.comments().list(**kwargs).execute()
    
    while results:
        for item in results['items']:
            
            one_comment = []
            
            id_comment =  item['id']

            user_name = item['snippet']['authorDisplayName']
            comment = remove_tags(item['snippet']['textDisplay'].replace('\r', ''))
            youtube_channel = item['snippet']['authorChannelUrl']
            publishedAt = item['snippet']['publishedAt']
            updatedAt = item['snippet']['updatedAt']
            
            one_comment.append(id_comment)
            one_comment.append(youtube_channel)
            one_comment.append(user_name)
            one_comment.append(publishedAt)
            one_comment.append(updatedAt) 
            one_comment.append(comment)
            
            comments.append(one_comment)
            
        if 'nextPageToken' in results:
            kwargs['pageToken'] = results['nextPageToken']
            results = service.one_comment().list(**kwargs).execute()
            
        else:
            break

    return comments


def add_comments_to_list(video_from_channel, count_request, service):
    count_request += 2 # use for APIs
    urlss = video_from_channel
    list_of_comments = []

    a = get_video_comments_1(service, videoId=urlss, part="snippet", maxResults=100)
    count_request += 2
    for i in a[0]:
        
        list_of_comments.append(i)
    #----------------------counter for change api
    print(count_request)
    try:
        if count_request > 8000:
            api_key = next(keys)
            print('using new API ')
            service = build('youtube', 'v3', developerKey=api_for_compare)
            count_request = 0
    except StopIteration:
        print("api's run out")
    #----------------------
    for i in a[1]:
        b = get_comments_from_comment(service, parentId=i, part="snippet", maxResults=100)
        count_request += 2
        for j in b:

            list_of_comments.append(j)
    return list_of_comments, count_request


def add_comments_to_database(url):
    
    # count_request preferably take from database which number will zeros every 24 hours  
    list_of_comments, count_request = add_comments_to_list(url.split('/')[-1].replace('watch?v=', ''),0,service)
    for item in list_of_comments:
        b = Comments(   id_comment=item[0],
                        youtube_url=url,
                        youtube_url_channel=item[1], 
                        nickname=item[2], 
                        date_published_comment=item[3], 
                        date_updated_comment=item[4], 
                        comment=item[5])
        b.save()
    
    return 1


# Define a view
class CommentsListView(ListView):
    # print info from database to tamplates
    global url_for_compare
    model = Comments
    fields = ['id_comment','youtube_url','youtube_url_channel','nickname','date_published_comment','date_updated_comment', 'comment']
    template_name = 'frontpage/comments_list.html'
    
    # pass through variable request.POST  from one template to another
    # need for {% if comments.youtube_url == compare_youtube_url %} in comments.html 
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['compare_youtube_url'] = url_for_compare
        return context
 

def check_url_for_exist_in_database(url_for_compare, api_for_compare):
    # Compare sum of comments from url link and from database
    # If equal do nothing, if not - delete records from database filter by youtube_url
    # and reload
    url = "https://www.googleapis.com/youtube/v3/videos?part=statistics&id="+url_for_compare.split('/')[-1].replace('watch?v=', '')+"&key="+api_for_compare
    response = urlopen(url)
    data_json = json.loads(response.read())
    count_comments = data_json['items'][0]['statistics']['commentCount']
    count_comments_in_database = Comments.objects.filter(youtube_url__startswith=url_for_compare)
    print(count_comments)
    print(len(count_comments_in_database))

    if int(count_comments) == len(count_comments_in_database):
        print("count_comments = ",count_comments)
        print("count_comments_in_database = ",count_comments_in_database)

    else:
        print(count_comments_in_database)
        count_comments_in_database.delete()
        print("Delete comments")
        ## UNCOMMENT FOR WORK WITH DATABASE!!!!
        return add_comments_to_database(url_for_compare)










     