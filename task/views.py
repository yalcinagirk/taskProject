from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

from task.serializers import TaskSerializer, SurveySerializer, UnlabeledSerializer, LabelSerializer
from task.models import Task
from unlabeled.models import UnLabeledData
from label.models import Label
from survey.models import Survey


################### TASK ###################

class TaskListView(ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskCreateView(CreateAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

################### SURVEY ###################

class BaseSurveyView(APIView):
    def get_queryset(self):
        task_id = self.kwargs['task_id']
        qs = super(SurveyListView, self).get_queryset()
        if qs.exists():
            qs = qs.filter(task__id=task_id).order_by('id')
        return qs


class SurveyListView(ListAPIView, BaseSurveyView):
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer

    

class SurveyCreateView(CreateAPIView, BaseSurveyView):
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer

################### UBLABELED ###################

class BaseUnlabeledView(APIView):
    def get_queryset(self):
        task_id = self.kwargs.get('task_id')
        qs = super(UnlabeledListView, self).get_queryset()
        if qs.exists():
            qs = qs.filter(surveyy__task__id=task_id).order_by('id')
        return qs


class UnlabeledListView(ListAPIView, BaseUnlabeledView):
    queryset = UnLabeledData.objects.all()
    serializer_class = UnlabeledSerializer


class UnlabeledCreateView(CreateAPIView, BaseUnlabeledView):
    queryset = UnLabeledData.objects.all()
    serializer_class = UnlabeledSerializer

################### LABEL ###################

class BaseLabelView(APIView):
    def get_queryset(self):
        task_id = self.kwargs.get('task_id')
        qs = super(LabelListView, self).get_queryset()
        if qs.exists():
            qs = qs.filter(surveyy__task__id=task_id).order_by('id')
        return qs


class LabelListView(ListAPIView):
    queryset = Label.objects.all()
    serializer_class = LabelSerializer


class LabelCreateView(CreateAPIView):
    queryset = Label.objects.all()
    serializer_class = LabelSerializer
