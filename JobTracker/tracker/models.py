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
