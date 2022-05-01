from django.db import models
from django.contrib.auth.models import User

from survey.models import Survey


class Label(models.Model):
    id = models.AutoField(primary_key=True)
    created_by  = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    surveyy = models.ForeignKey(Survey, null=True, on_delete=models.SET_NULL)
    order = models.PositiveIntegerField(unique=True)
    checked = models.BooleanField(default=False)
    text = models.CharField(max_length=120)

    def __str__(self):
        return "{0} - {1} - {2}".format(self.order, self.checked, self.text)