from django.shortcuts import render, redirect
from django.views.generic import (View, UpdateView, TemplateView,
                                 ListView, CreateView, DeleteView)
# Create your views here.
from task.models import Task
from django.urls import reverse_lazy, reverse
from django import http
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin

class taskList(LoginRequiredMixin, ListView):
    template_name = "task/tasklist.html"
    model = Task

class addTaskView(LoginRequiredMixin, CreateView):
    template_name = "task/addtask.html"
    model = Task
    fields = ['query', 'response', 'status', 'correct']
    success_url = reverse_lazy('task:tasklist')

class updateTaskView(LoginRequiredMixin, UpdateView):
    template_name = "task/updatetask.html"
    model = Task
    fields = ['query', 'response', 'status', 'correct']
    success_url = reverse_lazy('task:tasklist')

class deleteTaskView(LoginRequiredMixin, View):
    model = Task
    

    def get(self, request, pk, **kwargs):
        obj = get_object_or_404(self.model, pk=pk)
        obj.delete()
        
        return redirect('task:tasklist')
    


