from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    headImage = models.FileField(upload_to='upload/headImage/')
    def __unicode__(self):
        return self.username


class Video(models.Model):
    entry = models.ForeignKey(User)
    videoname = models.CharField(max_length=30)
    videokeyworld = models.CharField(max_length=30)
    videoclass = models.CharField(max_length=30)
    videodescribe = models.CharField(max_length=30)
    videosource = models.FileField(upload_to='upload/video/')
