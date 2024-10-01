# tracker/forms.py
from django import forms
from .models import JobApplication, JobPosting, Document

class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ['job_posting', 'resume', 'cover_letter', 'additional_documents', 'notes', 'status']
        widgets = {
            'job_posting': forms.TextInput(attrs={'class': 'form-control', 'autocomplete': 'off', 'readonly': 'readonly'}),
            'resume': forms.Select(attrs={'class': 'form-control'}),
            'cover_letter': forms.Select(attrs={'class': 'form-control'}),
            'additional_documents': forms.Select(attrs={'class': 'form-control'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 8}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(JobApplicationForm, self).__init__(*args, **kwargs)
        
        # Define allowed document types
        allowed_resume_types = ['resume']
        allowed_cover_letter_types = ['cover_letter']
        allowed_additional_document_types = ['other']

        # Filter the queryset for each field
        self.fields['resume'].queryset = Document.objects.filter(document_type__in=allowed_resume_types)
        self.fields['cover_letter'].queryset = Document.objects.filter(document_type__in=allowed_cover_letter_types)
        self.fields['additional_documents'].queryset = Document.objects.filter(document_type__in=allowed_additional_document_types)

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
