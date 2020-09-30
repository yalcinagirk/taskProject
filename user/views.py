from django.urls import reverse, reverse_lazy
from django.shortcuts import render, redirect
from django.views.generic import ListView, UpdateView, View, CreateView
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
# Create your views here.


class userLogin(LoginView):
    form_class = AuthenticationForm
    template_name = 'login.html'
    success_url = 'tasklist'
    redirect_authenticated_user= True


class userLogout(LoginRequiredMixin, LogoutView):
    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)

class userList(LoginRequiredMixin, ListView):
    model = User
    template_name = 'userlist.html'


class userUpdate(LoginRequiredMixin, UpdateView):
    model = User
    fields = {'username', 'password', 'email', 'first_name', 'last_name'}
    template_name = 'userupdate.html'
    success_url = reverse_lazy('user:userlist')

class userCreate(LoginRequiredMixin, CreateView):
    form_class = UserCreationForm
    template_name = 'usercreate.html'
    success_url = reverse_lazy('user:userlist')

class userDelete(LoginRequiredMixin, View):
    model = User

    def get(self, request, pk, **kwargs):
        user = get_object_or_404(self.model, pk=pk)
        user.delete()
        
        return redirect('user:userlist')
    



    
