from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from secrets import token_urlsafe


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.CharField(max_length=200)
    created_post_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.title} - {self.text} - {self.created_post_date}"
