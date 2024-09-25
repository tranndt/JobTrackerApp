# tracker/models.py
from django.db import models

class JobApplication(models.Model):
    company_name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    job_url = models.URLField(max_length=500, blank=True)
    resume = models.FileField(upload_to='resumes/')
    cover_letter = models.FileField(upload_to='cover_letters/')
    application_date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=[
        ('Applied', 'Applied'),
        ('Interview', 'Interview'),
        ('Rejected', 'Rejected'),
        ('Offer', 'Offer'),
    ], default='Applied')
    notes = models.TextField(blank=True)
    
    def __str__(self):
        return f'{self.position} at {self.company_name}'

from geopy.geocoders import Nominatim
from django.utils import timezone

class JobPosting(models.Model):
    company_name = models.CharField(max_length=255, blank="Untitled Company")
    job_title = models.CharField(max_length=255, blank="Untitled Job")  # New field
    posting_url = models.URLField(max_length=500, blank="None")  # New field for job posting URL
    location = models.CharField(max_length=255, blank="Unspecified")  # Changed from address to location
    is_remote = models.BooleanField(default=False)  # New field for remote work
    description = models.TextField(blank="No description provided")
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    date_created = models.DateTimeField(default=timezone.now)  # Auto-generated field

    def save(self, *args, **kwargs):
        # Geocode location into latitude and longitude
        if not self.latitude or not self.longitude:
            geolocator = Nominatim(user_agent="job_tracker_app")
            location = geolocator.geocode(self.location)
            if location:
                self.latitude = location.latitude
                self.longitude = location.longitude
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.company_name} - {self.job_title}"
    




class Document(models.Model):
    # Define choices for document types
    DOCUMENT_TYPE_CHOICES = [
        ('resume', 'Resume'),
        ('cover_letter', 'Cover Letter'),
        ('other', 'Other'),
    ]
    
    document_type = models.CharField(max_length=20, choices=DOCUMENT_TYPE_CHOICES)
    document_name = models.CharField(max_length=255, blank="Untitled Document", null=True)
    file = models.FileField(upload_to='documents/', blank=True, null=True)
    text_content = models.TextField(blank=True, null=True)
    date_uploaded = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.get_document_type_display()} uploaded on {self.date_uploaded.strftime('%Y-%m-%d %H:%M:%S')}"
    
    def save(self, *args, **kwargs):
        if self.file and self.document_name == "Untitled Document":
            self.document_name = str(self.file)
        super().save(*args, **kwargs)

