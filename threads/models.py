from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

#Ideas for the future: Prizes with coins

class Thread(models.Model):
    title = models.CharField(max_length = 300)
    text = models.TextField()
    image = models.ImageField(default="def_image.png", upload_to="thread_images")
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    publish_date = models.DateTimeField(default=timezone.now)

class Reply(models.Model):
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE, related_name='replies')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    #image = models.ImageField(default="def_image.png", upload_to="reply_images")
    publish_date = models.DateTimeField(default=timezone.now)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    icon = models.ImageField(default="def_pfp.png", upload_to="profile_pics")

