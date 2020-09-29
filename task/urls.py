
from django.contrib import admin
from django.urls import path, include

from task.views import taskList, addTaskView, deleteTaskView, updateTaskView
app_name = 'task'
urlpatterns = [
    path('tasklist', taskList.as_view(), name='tasklist'),
    path('addtask', addTaskView.as_view(), name='addtag'),
    path('<int:pk>/update/', updateTaskView.as_view(), name='taskupdate'),
    path('<int:pk>/delete/', deleteTaskView.as_view(), name='taskdelete'),
] 
