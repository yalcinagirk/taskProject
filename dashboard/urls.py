from django.urls import path, include
from dashboard.views import homeView
app_name = 'dashboard'
urlpatterns = [
    path('', homeView.as_view(), name='home'),
]
