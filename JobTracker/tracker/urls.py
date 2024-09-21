# tracker/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('new/', views.create_application, name='create_application'),
    path('dashboard/', views.dashboard, name='dashboard'),
]
