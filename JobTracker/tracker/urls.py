# tracker/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('new/', views.create_posting, name='create_posting'),
    path('', views.dashboard, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('delete/<int:pk>/', views.delete_posting, name='delete_posting'),
    path('view/<int:pk>/', views.view_posting, name='view_posting'),
    path('edit/<int:pk>/', views.create_posting, name='edit_posting'),  # New edit route
    path('map/', views.map_view, name='map_view'),
    path('import-from-url/', views.import_from_url_view, name='import_from_url'),
    path('upload-files/', views.upload_files, name='upload_files'),
    path('documents/', views.view_all_documents, name='view_all_documents'),
    path('documents/<int:document_id>/', views.view_document, name='view_document'),
]
