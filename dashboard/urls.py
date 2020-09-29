from django.urls import path, include
from dashboard.views import homeView
urlpatterns = [
    path('', homeView.as_view(), name='dashboard'),
]
