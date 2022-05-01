from django.urls import path, include

# from api.views

urlpatterns = [
    path('task/', include('task.urls')),
    path('survey/', include('survey.urls')),
    path('unlabeled/', include('unlabeled.urls')),
    path('label/', include('label.urls')),
    path('user/', include('user.urls')),
]
