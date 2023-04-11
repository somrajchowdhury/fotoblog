from django.db import models
from django.conf import settings

class Photo(models.Model):
    image = models.ImageField()
    caption = models.CharField(max_length=128,
                               blank=True)
    uploader = models.ForeignKey(to=settings.AUTH_USER_MODEL,
                                 on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

class Blog(models.Model):
    photo = models.ForeignKey(to=Photo,
                              on_delete=models.SET_NULL,
                              blank=True,
                              null=True)
    title = models.CharField(max_length=128)
    content = models.CharField(max_length=5000)
    author = models.ForeignKey(to=settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    starred = models.BooleanField(default=False)
