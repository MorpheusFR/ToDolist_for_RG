from datetime import datetime, date
from django.contrib import auth
from django.contrib.auth.models import User
import time
from django.utils import timezone

from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    creator = models.ForeignKey(User)
    created_at = models.DateTimeField(default=datetime.now(), blank=True)
    finished_at = models.DateTimeField(default=datetime.now(), blank=True)
    finished = models.BooleanField(default=False)
    priority = models.IntegerField(default=0)
    deadline = models.DateField(default=date.today(), blank=True)

    def __str__(self): #this is to return the name of the object.
        return self.title