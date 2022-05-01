from django.urls import path

from user.views import UserListView, UserCreateView

urlpatterns = [
    path('list', UserListView.as_view(), name='user_list'),
    path('create', UserCreateView.as_view(), name='user_create')
]
