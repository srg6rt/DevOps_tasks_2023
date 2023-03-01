from django import forms

class URLForm(forms.Form):
    paste_youtube_url = forms.CharField(label='Youtube URL', max_length=100)