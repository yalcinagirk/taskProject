
from django.contrib import admin
from django.urls import path, include

from user.views import userLogin, userLogout, userList, userUpdate,  userDelete, userCreate
app_name = 'user'
urlpatterns = [
    path('login', userLogin.as_view(), name='login'),
    path('<int:id>/logout', userLogout.as_view(), name='logout'),
    path('userlist', userList.as_view(), name='userlist'),
    path('usercreate', userCreate.as_view(), name='usercreate'),
    path('<int:pk>/update', userUpdate.as_view(), name='update'),
    path('<int:pk>/delete', userDelete.as_view(), name='delete'),
] 
