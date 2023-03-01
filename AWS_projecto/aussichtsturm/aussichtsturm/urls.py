from django.contrib import admin
from django.urls import path
from youtube_comments_grabber import views
from django.conf.urls.static import static  
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('upload/', views.get_youtube_url, name='get_youtube_url'),
    path('comments/', views.CommentsListView.as_view(), name='comments'),

]
 