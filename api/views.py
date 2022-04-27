from pickle import NONE
from rest_framework.generics import ListAPIView
# Create your views here.

from django.contrib.auth.models import User

from api.serializers import UserListSerializer


class UserListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer
