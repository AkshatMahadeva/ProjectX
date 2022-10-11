from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

class Post(models.Model):
    sno=models.AutoField(primary_key=True)
    title=models.CharField(max_length=255)
    image = models.ImageField(upload_to='blog/images', default="")
    author=models.CharField(User, max_length=14)
    slug=models.CharField(max_length=130)
    timeStamp=models.DateTimeField(default=now)
    content=models.TextField()

    def __str__(self):
        return self.title + " by " + self.author