# tracker/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('new/', views.create_posting, name='create_posting'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('view/<int:posting_id>/', views.view_posting, name='view_posting'),
    path('delete/<int:posting_id>/', views.delete_posting, name='delete_posting'),
    path('map/', views.map_view, name='map_view'),
]
