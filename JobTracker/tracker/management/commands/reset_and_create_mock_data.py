# tracker/management/commands/reset_and_create_mock_data.py
from django.core.management.base import BaseCommand
from tracker.models import JobPosting, JobApplication, Document
from datetime import datetime
from django.utils import timezone

class Command(BaseCommand):
    help = 'Delete entire database and instantiate with mock data'

    def handle(self, *args, **kwargs):
        # Delete all existing data
        JobApplication.objects.all().delete()
        JobPosting.objects.all().delete()
        Document.objects.all().delete()

        # Create mock documents
        documents = [
            Document.objects.create(file='https://example.com/resume/johndoe.pdf', document_type='resume', document_name='John Doe Resume', text_content='John Doe Resume Content', date_uploaded=timezone.now()),
            Document.objects.create(file='https://example.com/cover_letter/johndoe.pdf', document_type='cover_letter', document_name='John Doe Cover Letter', text_content='John Doe Cover Letter Content', date_uploaded=timezone.now()),
            Document.objects.create(file='https://example.com/portfolio/johndoe.pdf', document_type='other', document_name='John Doe Portfolio', text_content='John Doe Portfolio Content', date_uploaded=timezone.now()),

            Document.objects.create(file='https://example.com/resume/janesmith.pdf', document_type='resume', document_name='Jane Smith Resume', text_content='Jane Smith Resume Content', date_uploaded=timezone.now()),
            Document.objects.create(file='https://example.com/cover_letter/janesmith.pdf', document_type='cover_letter', document_name='Jane Smith Cover Letter', text_content='Jane Smith Cover Letter Content', date_uploaded=timezone.now()),
            Document.objects.create(file='https://example.com/portfolio/janesmith.pdf', document_type='other', document_name='Jane Smith Portfolio', text_content='Jane Smith Portfolio Content', date_uploaded=timezone.now()),

            Document.objects.create(file='https://example.com/resume/alicejohnson.pdf', document_type='resume', document_name='Alice Johnson Resume', text_content='Alice Johnson Resume Content', date_uploaded=timezone.now()),
            Document.objects.create(file='https://example.com/cover_letter/alicejohnson.pdf', document_type='cover_letter', document_name='Alice Johnson Cover Letter', text_content='Alice Johnson Cover Letter Content', date_uploaded=timezone.now()),
            Document.objects.create(file='https://example.com/portfolio/alicejohnson.pdf', document_type='other', document_name='Alice Johnson Portfolio', text_content='Alice Johnson Portfolio Content', date_uploaded=timezone.now()),

            Document.objects.create(file='https://example.com/resume/bobbrown.pdf', document_type='resume', document_name='Bob Brown Resume', text_content='Bob Brown Resume Content', date_uploaded=timezone.now()),
            Document.objects.create(file='https://example.com/cover_letter/bobbrown.pdf', document_type='cover_letter', document_name='Bob Brown Cover Letter', text_content='Bob Brown Cover Letter Content', date_uploaded=timezone.now()),
            Document.objects.create(file='https://example.com/portfolio/bobbrown.pdf', document_type='other', document_name='Bob Brown Portfolio', text_content='Bob Brown Portfolio Content', date_uploaded=timezone.now()),

            Document.objects.create(file='https://example.com/resume/carolwhite.pdf', document_type='resume', document_name='Carol White Resume', text_content='Carol White Resume Content', date_uploaded=timezone.now()),
            Document.objects.create(file='https://example.com/cover_letter/carolwhite.pdf', document_type='cover_letter', document_name='Carol White Cover Letter', text_content='Carol White Cover Letter Content', date_uploaded=timezone.now()),
            Document.objects.create(file='https://example.com/portfolio/carolwhite.pdf', document_type='other', document_name='Carol White Portfolio', text_content='Carol White Portfolio Content', date_uploaded=timezone.now()),
        ]

        # Create mock job postings
        job_postings = [
            JobPosting.objects.create(job_title='Software Developer', company_name='Tech Corp', location='New York', description='Develop software solutions.', date_created=timezone.now()),
            JobPosting.objects.create(job_title='Data Analyst', company_name='Data Inc', location='San Francisco', description='Analyze data trends.', date_created=timezone.now()),
            JobPosting.objects.create(job_title='Machine Learning Engineer', company_name='AI Labs', location='Boston', description='Develop ML models.', date_created=timezone.now()),
            JobPosting.objects.create(job_title='Financial Analyst', company_name='Finance Group', location='Chicago', description='Analyze financial data.', date_created=timezone.now()),
            JobPosting.objects.create(job_title='UX Designer', company_name='Design Studio', location='Los Angeles', description='Design user experiences.', date_created=timezone.now()),
        ]

        # Create mock job applications
        mock_applications = [
            {
                'resume': documents[0],
                'cover_letter': documents[1],
                'additional_documents': documents[2],
                'job_posting': job_postings[0],
                'status': 'Pending',
                'notes': 'First round interview scheduled.'
            },
            {
                'resume': documents[3],
                'cover_letter': documents[4],
                'additional_documents': documents[5],
                'job_posting': job_postings[1],
                'status': 'Pending',
                'notes': 'Waiting for feedback.'
            },
            {
                'resume': documents[6],
                'cover_letter': documents[7],
                'additional_documents': documents[8],
                'job_posting': job_postings[2],
                'status': 'Pending',
                'notes': 'Technical interview completed.'
            },
            {
                'resume': documents[9],
                'cover_letter': documents[10],
                'additional_documents': documents[11],
                'job_posting': job_postings[3],
                'status': 'Pending',
                'notes': 'HR interview scheduled.'
            },
            {
                'resume': documents[12],
                'cover_letter': documents[13],
                'additional_documents': documents[14],
                'job_posting': job_postings[4],
                'status': 'Pending',
                'notes': 'Background check in progress.'
            },
        ]

        for application in mock_applications:
            JobApplication.objects.create(
                job_posting=application['job_posting'],
                resume=application['resume'],
                cover_letter=application['cover_letter'],
                additional_documents=application['additional_documents'],
                application_date=datetime.now(),
                status=application['status'],
                notes=application['notes']
            )

        self.stdout.write(self.style.SUCCESS('Successfully reset database and created mock data'))