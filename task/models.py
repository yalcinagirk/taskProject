from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    id = models.AutoField(primary_key=True)
    created_by  = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='created_by')
    assigned = models.ManyToManyField(User, related_name='assigned')
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name
