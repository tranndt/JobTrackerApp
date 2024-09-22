# tracker/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .forms import JobApplicationForm, JobPostingForm
from .models import JobApplication, JobPosting
from django.core.serializers import serialize
from geopy.geocoders import Nominatim
from django.contrib import messages
from geopy.exc import GeocoderServiceError

def create_posting(request, pk=None):
    if pk:
        # Editing an existing posting
        posting = get_object_or_404(JobPosting, pk=pk)
        if request.method == 'POST':
            form = JobPostingForm(request.POST, instance=posting)
            if form.is_valid():
                # Validate location before saving
                if not form.cleaned_data['is_remote']:
                    geolocator = Nominatim(user_agent="job_tracker_app")
                    try:
                        location = geolocator.geocode(form.cleaned_data['location'])
                        if location:
                            form.save()
                            return redirect('dashboard')
                        else:
                            return render(request, 'tracker/create_posting.html', {
                                'form': form,
                                'error': 'Invalid location. Please enter a valid address.'
                            })
                    except GeocoderServiceError:
                        return render(request, 'tracker/create_posting.html', {
                            'form': form,
                            'error': 'Geocoding service failed. Please try again.'
                        })
                else:
                    form.save()  # Save without geocoding for remote jobs
                    return redirect('dashboard')
        else:
            form = JobPostingForm(instance=posting)
    else:
        # Creating a new posting
        posting = None
        if request.method == 'POST':
            form = JobPostingForm(request.POST)
            if form.is_valid():
                if not form.cleaned_data['is_remote']:
                    geolocator = Nominatim(user_agent="job_tracker_app")
                    try:
                        location = geolocator.geocode(form.cleaned_data['location'])
                        if location:
                            form.save()
                            return redirect('dashboard')
                        else:
                            return render(request, 'tracker/create_posting.html', {
                                'form': form,
                                'error': 'Invalid location. Please enter a valid address.'
                            })
                    except GeocoderServiceError:
                        return render(request, 'tracker/create_posting.html', {
                            'form': form,
                            'error': 'Geocoding service failed. Please try again.'
                        })
                else:
                    form.save()  # Save without geocoding for remote jobs
                    return redirect('dashboard')
        else:
            form = JobPostingForm()

    return render(request, 'tracker/create_posting.html', {
        'form': form,
        'is_editing': pk is not None,
        'posting': posting
    })

def dashboard(request):
    postings = JobPosting.objects.all()
    return render(request, 'tracker/dashboard.html', {'postings': postings})

def map_view(request):
    job_postings = JobPosting.objects.all()
    job_postings_json = serialize('json', job_postings)
    return render(request, 'tracker/map_view.html', {'job_postings_json': job_postings_json})

def view_posting(request, pk):
    posting = JobPosting.objects.get(pk=pk)
    return render(request, 'tracker/view_posting.html', {'posting': posting})

from django.shortcuts import get_object_or_404

def delete_posting(request, pk):
    job_posting = JobPosting.objects.get(pk=pk)
    job_posting.delete()
    return redirect('dashboard')
