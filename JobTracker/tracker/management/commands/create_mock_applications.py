# tracker/management/commands/create_mock_applications.py
from django.core.management.base import BaseCommand
from tracker.models import JobPosting, JobApplication, Document
from datetime import datetime

class Command(BaseCommand):
    help = 'Create and initiate mock job applications for each job posting'

    def handle(self, *args, **kwargs):
        # Retrieve mock documents from the database by their IDs
        resume_johndoe = Document.objects.get(id=1)
        cover_letter_johndoe = Document.objects.get(id=1)
        portfolio_johndoe = Document.objects.get(id=1)

        resume_janesmith = Document.objects.get(id=2)
        cover_letter_janesmith = Document.objects.get(id=2)
        portfolio_janesmith = Document.objects.get(id=2)

        resume_alicejohnson = Document.objects.get(id=3)
        cover_letter_alicejohnson = Document.objects.get(id=3)
        portfolio_alicejohnson = Document.objects.get(id=3)

        resume_bobbrown = Document.objects.get(id=4)
        cover_letter_bobbrown = Document.objects.get(id=4)
        portfolio_bobbrown = Document.objects.get(id=4)

        resume_carolwhite = Document.objects.get(id=5)
        cover_letter_carolwhite = Document.objects.get(id=5)
        portfolio_carolwhite = Document.objects.get(id=5)

        mock_applications = [
            {
                'resume': resume_johndoe,
                'cover_letter': cover_letter_johndoe,
                'additional_documents': [portfolio_johndoe],
                'job_posting_id': 1,
                'status': 'Pending',
                'notes': 'First round interview scheduled.'
            },
            {
                'resume': resume_janesmith,
                'cover_letter': cover_letter_janesmith,
                'additional_documents': [portfolio_janesmith],
                'job_posting_id': 2,
                'status': 'Pending',
                'notes': 'Waiting for feedback.'
            },
            {
                'resume': resume_alicejohnson,
                'cover_letter': cover_letter_alicejohnson,
                'additional_documents': [portfolio_alicejohnson],
                'job_posting_id': 3,
                'status': 'Pending',
                'notes': 'Technical interview completed.'
            },
            {
                'resume': resume_bobbrown,
                'cover_letter': cover_letter_bobbrown,
                'additional_documents': [portfolio_bobbrown],
                'job_posting_id': 4,
                'status': 'Pending',
                'notes': 'HR interview scheduled.'
            },
            {
                'resume': resume_carolwhite,
                'cover_letter': cover_letter_carolwhite,
                'additional_documents': [portfolio_carolwhite],
                'job_posting_id': 5,
                'status': 'Pending',
                'notes': 'Background check in progress.'
            },
        ]

        for application in mock_applications:
            job_posting = JobPosting.objects.get(id=application['job_posting_id'])
            JobApplication.objects.create(
                job_posting=job_posting,
                resume=application['resume'],
                cover_letter=application['cover_letter'],
                additional_documents=application['additional_documents'],
                application_date=datetime.now(),
                status=application['status'],
                notes=application['notes']
            )

        self.stdout.write(self.style.SUCCESS('Successfully created mock job applications'))