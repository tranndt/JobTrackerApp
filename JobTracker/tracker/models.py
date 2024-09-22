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

class JobPosting(models.Model):
    company_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.latitude or not self.longitude:
            geolocator = Nominatim(user_agent="job_tracker_app")
            location = geolocator.geocode(self.address)
            if location:
                self.latitude = location.latitude
                self.longitude = location.longitude
        super().save(*args, **kwargs)