from django.db import models
from django.utils import timezone 
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class VidStream(models.Model):
    streamer = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    description = models.TextField(max_length=600)
    upload_date = models.DateTimeField(default=timezone.now)
    video = models.FileField(upload_to='')


    def __str__(self):
        return self.title 

    def get_absolute_url(self):
        return reverse("video-detail", kwargs={"pk": self.pk})

