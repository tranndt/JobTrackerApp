# tracker/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_jobs, name='home'),
    path('map/', views.map_view, name='map_view'),
    path('jobs/', views.all_jobs, name='all_jobs'),
    # path('jobs/new/', views.create_job, name='create_job'),
    path('jobs/new/', views.create_job, name='create_job'),  # New create route
    path('jobs/<int:job_id>/', views.view_job, name='view_job'),
    path('jobs/<int:job_id>/delete', views.delete_job, name='delete_job'),
    # path('jobs/<int:pk>/edit/', views.create_job, name='edit_posting'),  # New edit route
    path('jobs/<int:job_id>/edit/', views.edit_job, name='edit_job'),  # New edit route
    path('import-from-url/', views.import_from_url_view, name='import_from_url'),
    path('documents/', views.view_all_documents, name='view_all_documents'),
    path('documents/new/', views.create_document, name='create_document'),
    path('documents/<int:document_id>/', views.view_document, name='view_document'),
    path('documents/<int:document_id>/edit/', views.edit_document, name='edit_document'),
    path('documents/<int:document_id>/delete/', views.delete_document, name='delete_document'),
]
