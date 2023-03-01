from django.db import models

class Comments(models.Model):
	id_comment = models.CharField(max_length=200)
	youtube_url = models.CharField(max_length=200)
	youtube_url_channel = models.CharField(max_length=30)
	nickname = models.CharField(max_length=200)
	date_published_comment = models.CharField(max_length=50)
	date_updated_comment = models.CharField(max_length=50)
	comment = models.TextField()
	def __str__(self):
		return self.nickname
