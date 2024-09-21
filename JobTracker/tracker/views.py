# tracker/views.py
from django.shortcuts import render, redirect
from .forms import JobApplicationForm
from .models import JobApplication

def create_application(request):
    if request.method == 'POST':
        form = JobApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = JobApplicationForm()
    return render(request, 'tracker/create_application.html', {'form': form})

def dashboard(request):
    applications = JobApplication.objects.all()
    return render(request, 'tracker/dashboard.html', {'applications': applications})
