from django.urls import path

from task.views import *

urlpatterns = [
    path('list', TaskListView.as_view(), name='task_list'),
    path('create', TaskCreateView.as_view(), name='task_create'),

    ##### with task_id
    path('<int:task_id>/survey/list', SurveyListView.as_view(), name='survey_list'),
    path('<int:task_id>/survey/create', SurveyCreateView.as_view(), name='survey_create'),

    path('<int:task_id>/unlabeled/list', UnlabeledListView.as_view(), name='unlabeled_list'),
    path('<int:task_id>/unlabeled/create', UnlabeledCreateView.as_view(), name='unlabeled_create'),

    path('<int:task_id>/label/list', LabelListView.as_view(), name='label_list'),
    path('<int:task_id>/label/create', LabelCreateView.as_view(), name='label_create'),

]
