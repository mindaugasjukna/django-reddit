from django.db import models
from django.utils import timezone

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.CharField(max_length=200)
    created_post_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.title} - {self.text} - {self.created_post_date}"
