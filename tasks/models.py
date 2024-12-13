from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title

class OAuthKey(models.Model):
    key = models.CharField(max_length=255)
    value = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.description
