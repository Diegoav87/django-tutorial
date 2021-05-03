from django.db import models

# Create your models here.


class Post(models.Model):
    # image = models.ImageField()
    likes = models.PositiveIntegerField(default=0, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    quote = models.TextField(null=True, blank=True)


class Comment(models.Model):
    text = models.TextField()
