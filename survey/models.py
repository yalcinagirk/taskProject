from django.db import models
from django.contrib.auth.models import User

from task.models import Task


class Survey(models.Model):
    id = models.AutoField(primary_key=True)
    created_by  = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    task = models.ManyToManyField(Task)
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name