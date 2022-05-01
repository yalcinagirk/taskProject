from rest_framework import serializers

from task.models import Task
from unlabeled.models import UnLabeledData
from label.models import Label
from survey.models import Survey


class TaskSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Task
        fields = '__all__'


class SurveySerializer(serializers.ModelSerializer):    
    class Meta:
        model = Survey
        fields = '__all__'


class UnlabeledSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnLabeledData
        fields = '__all__'


class LabelSerializer(serializers.ModelSerializer):
    checked = serializers.BooleanField(read_only=True)
    class Meta:
        model = Label
        fields = '__all__'
