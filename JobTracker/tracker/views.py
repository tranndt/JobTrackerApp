# tracker/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .forms import JobApplicationForm, JobPostingForm, DocumentForm
from .models import JobApplication, JobPosting, Document
from django.core.serializers import serialize
from geopy.geocoders import Nominatim
from django.contrib import messages
from geopy.exc import GeocoderServiceError
from django.views.decorators.csrf import csrf_exempt
import os


# def create_job(request, pk=None):
#     if pk:
#         # Editing an existing posting
#         posting = get_object_or_404(JobPosting, pk=pk)
#         if request.method == 'POST':
#             form = JobPostingForm(request.POST, instance=posting)
#             if form.is_valid():
#                 # Validate location before saving
#                 if not form.cleaned_data['is_remote']:
#                     geolocator = Nominatim(user_agent="job_tracker_app")
#                     try:
#                         location = geolocator.geocode(form.cleaned_data['location'])
#                         if location:
#                             form.save()
#                             return redirect('all_jobs')
#                         else:
#                             return render(request, 'tracker/create_job.html', {
#                                 'form': form,
#                                 'error': 'Invalid location. Please enter a valid address.'
#                             })
#                     except GeocoderServiceError:
#                         return render(request, 'tracker/create_job.html', {
#                             'form': form,
#                             'error': 'Geocoding service failed. Please try again.'
#                         })
#                 else:
#                     form.save()  # Save without geocoding for remote jobs
#                     return redirect('all_jobs')
#         else:
#             form = JobPostingForm(instance=posting)
#     else:
#         # Creating a new posting
#         posting = None
#         if request.method == 'POST':
#             form = JobPostingForm(request.POST)
#             if form.is_valid():
#                 if not form.cleaned_data['is_remote']:
#                     geolocator = Nominatim(user_agent="job_tracker_app")
#                     try:
#                         location = geolocator.geocode(form.cleaned_data['location'])
#                         if location:
#                             form.save()
#                             return redirect('all_jobs')
#                         else:
#                             return render(request, 'tracker/create_job.html', {
#                                 'form': form,
#                                 'error': 'Invalid location. Please enter a valid address.'
#                             })
#                     except GeocoderServiceError:
#                         return render(request, 'tracker/create_job.html', {
#                             'form': form,
#                             'error': 'Geocoding service failed. Please try again.'
#                         })
#                 else:
#                     form.save()  # Save without geocoding for remote jobs
#                     return redirect('all_jobs')
#         else:
#             form = JobPostingForm()

#     return render(request, 'tracker/create_job.html', {
#         'form': form,
#         'is_editing': pk is not None,
#         'posting': posting
#     })

def create_job(request):
    if request.method == 'POST':
        form = JobPostingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_jobs')
    else:
        form = JobPostingForm()

    return render(request, 'tracker/create_job.html', {'form': form})

def edit_job(request, job_id):
    job = get_object_or_404(JobPosting, pk=job_id)
    if request.method == 'POST':
        form = JobPostingForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            messages.success(request, 'Job posting updated successfully!')
            return redirect('all_jobs')
    else:
        form = JobPostingForm(instance=job)
    return render(request, 'tracker/edit_job.html', {'form': form, 'job': job})


def all_jobs(request):
    jobs = JobPosting.objects.all()
    return render(request, 'tracker/all_jobs.html', {'jobs': jobs})

def map_view(request):
    job_postings = JobPosting.objects.all()
    job_postings_json = serialize('json', job_postings)
    return render(request, 'tracker/map_view.html', {'job_postings_json': job_postings_json})

# def view_job(request, job_id):
#     job = get_object_or_404(JobPosting, id=job_id)
#     documents = Document.objects.all()
#     document_form = DocumentForm()

#     if request.method == 'POST':
#         document_form = DocumentForm(request.POST, request.FILES)
#         if document_form.is_valid():
#             document_form.save()
#             # Handle the rest of the application creation logic here

#     context = {
#         'job': job,
#         'documents': documents,
#         'document_form': document_form,
#     }
#     return render(request, 'tracker/view_job.html', context)

def view_job(request, job_id):
    job = get_object_or_404(JobPosting, id=job_id)
    job_application = JobApplication.objects.filter(job_posting=job).first()
    
    return render(request, 'tracker/view_job.html', {
        'job': job,
        'job_application': job_application,
    })

def delete_job(request, job_id):
    job = get_object_or_404(JobPosting, id=job_id)
    if request.method == 'POST':
        job.delete()
        # messages.success(request, 'Job deleted successfully!')
        return redirect('all_jobs')
    return render(request, 'tracker/delete_job.html', {'job': job})

from django.http import JsonResponse
from .functions import import_from_url

def import_from_url_view(request):
    if request.method == 'POST':
        url = request.POST.get('url')
        if not url:
            return JsonResponse({'error': 'URL is required'}, status=400)
        
        job_data = import_from_url(url)
        if isinstance(job_data, str):  # If an error occurred, the function returns a string message
            return JsonResponse({'error': job_data}, status=400)
        else:
            return JsonResponse(job_data)
    else:
        return render(request, 'tracker/import_from_url_view.html')
    
from .forms import DocumentForm

def create_document(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            # Ensure either file or text_content is provided
            if not form.cleaned_data['file'] and not form.cleaned_data['text_content']:
                messages.error(request, 'Please provide either a file or text content.')
            else:
                form.save()
                # messages.success(request, f'Document {form.cleaned_data["document_name"]} uploaded successfully.')
                return redirect('view_all_documents')
        else:
            messages.error(request, 'Failed to upload document. Please check the form for errors.')
    else:
        form = DocumentForm()

    return render(request, 'tracker/create_document.html', {'form': form})


def view_all_documents(request):
    # Query documents by type
    resumes = Document.objects.filter(document_type='resume').order_by('-date_uploaded')
    cover_letters = Document.objects.filter(document_type='cover_letter').order_by('-date_uploaded')
    others = Document.objects.filter(document_type='other').order_by('-date_uploaded')

    # Render the template with grouped documents
    return render(request, 'tracker/view_all_documents.html', {
        'resumes': resumes,
        'cover_letters': cover_letters,
        'others': others,
    })

def view_document(request, document_id):
    # Retrieve the specific document by ID
    document = get_object_or_404(Document, id=document_id)
    
    # Render the document details
    return render(request, 'tracker/view_document.html', {'document': document})


def edit_document(request, document_id):
    document = get_object_or_404(Document, id=document_id)
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES, instance=document)
        if form.is_valid():
            form.save()
            messages.success(request, 'Document updated successfully!')
            return redirect('view_all_documents')
    else:
        form = DocumentForm(instance=document)
    return render(request, 'tracker/edit_document.html', {'form': form, 'document': document})


def delete_document(request, document_id):
    document = get_object_or_404(Document, id=document_id)
    
    if request.method == 'POST':
        # Get the file path
        if document.file:
            file_path = document.file.path
            
            # Delete the file from the filesystem
            if os.path.exists(file_path):
                os.remove(file_path)
        
        # Delete the document entry from the database
        document.delete()
        
        # Redirect to a success page or another appropriate view
        return redirect('view_all_documents')
    
    return render(request, 'tracker/delete_document.html', {'document': document})

def create_application(request, job_id):
    job = get_object_or_404(JobPosting, id=job_id)
    if request.method == 'POST':
        job_application_form = JobApplicationForm(request.POST)
        
        if job_application_form.is_valid():
            job_application = job_application_form.save(commit=False)
            job_application.job_posting = job
            job_application.save()
            return redirect('all_jobs')  # Assuming you have a view to list all jobs
    else:
        job_application_form = JobApplicationForm(initial={'job_posting': job})

    return render(request, 'tracker/create_application.html', {
        'job_application_form': job_application_form,
        'job': job,
    })

def view_application(request, job_id):
    job_application = get_object_or_404(JobApplication, job_posting_id=job_id)
    return render(request, 'tracker/view_application.html', {'job_application': job_application})

def edit_application(request, job_id):
    job_application = get_object_or_404(JobApplication, job_posting_id=job_id)
    
    if request.method == 'POST':
        job_application_form = JobApplicationForm(request.POST, instance=job_application)
        
        if job_application_form.is_valid():
            job_application_form.save()
            return redirect('view_application', job_id=job_id)
    else:
        job_application_form = JobApplicationForm(instance=job_application)
    return render(request, 'tracker/edit_application.html', {
        'job_application_form': job_application_form,
        'job_application': job_application,
    })