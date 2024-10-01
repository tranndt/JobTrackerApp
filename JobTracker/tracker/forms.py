# tracker/forms.py
from django import forms
from .models import JobApplication, JobPosting

class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ['job_posting', 'resume', 'cover_letter', 'additional_documents', 'notes', 'status']
        widgets = {
            'job_posting': forms.Select(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'resume': forms.Select(attrs={'class': 'form-control'}),
            'cover_letter': forms.Select(attrs={'class': 'form-control'}),
            'additional_documents': forms.Select(attrs={'class': 'form-control'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 8}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }

class JobPostingForm(forms.ModelForm):
    class Meta:
        model = JobPosting
        fields = ['posting_url', 'job_title','company_name', 'location', 'is_remote', 'description']  # Include 'is_remote'
        widgets = {
            'posting_url': forms.URLInput(attrs={'class': 'form-control', 'autocomplete': 'off'}),
            'company_name': forms.TextInput(attrs={'class': 'form-control', 'autocomplete': 'off'}),
            'job_title': forms.TextInput(attrs={'class': 'form-control', 'autocomplete': 'off'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'autocomplete': 'off'}),
            # 'is_remote': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 8, 'autocomplete': 'off'}),
        }

from .models import Document

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['document_name', 'document_type', 'file', 'text_content']
        widgets = {
            'document_name': forms.TextInput(attrs={'class': 'form-control', 'autocomplete': 'off'}),
            'document_type': forms.Select(attrs={'class': 'form-control'}),
            'file': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'text_content': forms.Textarea(attrs={'class': 'form-control', 'rows': 8}),
        }
