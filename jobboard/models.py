from django.db import models
from django.utils import timezone


class Message(models.Model):
    name = models.CharField(max_length=200)
    jobDesc = models.TextField()
    date = models.DateTimeField(default=timezone.now)
