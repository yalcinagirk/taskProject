from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    query = models.CharField(max_length=150)
    response = models.CharField(max_length=150)
    status = models.BooleanField(default=True)
    correct = models.CharField(max_length=150, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.query