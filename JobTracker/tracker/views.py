# tracker/views.py
from django.shortcuts import render, redirect
from .forms import JobApplicationForm, JobPostingForm
from .models import JobApplication, JobPosting
from django.core.serializers import serialize
from geopy.geocoders import Nominatim
from django.contrib import messages

def create_posting(request):
    if request.method == 'POST':
        form = JobPostingForm(request.POST)
        if form.is_valid():
            # Get the address and try to geocode
            address = form.cleaned_data['address']
            geolocator = Nominatim(user_agent="job_tracker_app")
            location = geolocator.geocode(address)

            if location:
                # If valid coordinates, proceed to save the object
                posting = form.save(commit=False)
                posting.latitude = location.latitude
                posting.longitude = location.longitude
                posting.save()

                # Stay on the form and display a success message
                messages.success(request, 'Job posting created successfully!')
            else:
                # If no valid location, show an error message
                messages.error(request, 'Invalid address, please provide a valid address.')
    else:
        form = JobPostingForm()

    return render(request, 'tracker/create_posting.html', {'form': form})


def dashboard(request):
    job_postings = JobPosting.objects.all()
    return render(request, 'tracker/dashboard.html', {'job_postings': job_postings})

def map_view(request):
    job_postings = JobPosting.objects.all()
    job_postings_json = serialize('json', job_postings)
    return render(request, 'tracker/map_view.html', {'job_postings_json': job_postings_json})

def view_posting(request, posting_id):
    job_posting = JobPosting.objects.get(id=posting_id)
    return render(request, 'tracker/view_posting.html', {'job_posting': job_posting})

from django.shortcuts import get_object_or_404

def delete_posting(request, posting_id):
    job_posting = get_object_or_404(JobPosting, id=posting_id)
    job_posting.delete()
    messages.success(request, 'Job posting deleted successfully!')
    return redirect('dashboard')
