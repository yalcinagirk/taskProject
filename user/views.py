from rest_framework import serializers
from rest_framework.generics import ListAPIView, CreateAPIView
from django.contrib.auth.models import User

from user.serializers import UserSerializer


class UserListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserCreateView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
