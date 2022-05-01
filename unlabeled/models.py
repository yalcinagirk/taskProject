from django.db import models

from django.contrib.auth.models import User


class UnLabeledData(models.Model):
    id = models.AutoField(primary_key=True)
    created_by  = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    user = models.ManyToManyField(User, related_name='user')
    text = models.TextField()

    def __str__(self):
        return self.text