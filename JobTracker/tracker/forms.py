# tracker/forms.py
from django import forms
from .models import JobApplication, JobPosting

class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ['company_name', 'position', 'job_url', 'resume', 'cover_letter', 'status', 'notes']

class JobPostingForm(forms.ModelForm):
    class Meta:
        model = JobPosting
        fields = ['company_name', 'address']
