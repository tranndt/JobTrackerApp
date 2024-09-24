# tracker/management/commands/create_mock_postings.py
from django.core.management.base import BaseCommand
from tracker.models import JobPosting
from datetime import datetime

class Command(BaseCommand):
    help = 'Create and initiate 5 mock job postings'

    def handle(self, *args, **kwargs):
        mock_postings = [
            {
                'company_name': 'Tech Innovators Inc.',
                'job_title': 'Software Developer',
                'posting_url': 'https://techinnovators.com/careers/software-developer',
                'location': 'Winnipeg, MB',
                'description': 'Develop and maintain web applications. Work with a team of developers.',
                'is_remote': False,
            },
            {
                'company_name': 'Green Energy Solutions',
                'job_title': 'Data Analyst',
                'posting_url': 'https://greenenergy.com/jobs/data-analyst',
                'location': 'Remote',
                'description': 'Analyze data to improve energy efficiency. Remote work allowed.',
                'is_remote': True,
            },
            {
                'company_name': 'HealthTech Corp.',
                'job_title': 'Machine Learning Engineer',
                'posting_url': 'https://healthtechcorp.com/careers/ml-engineer',
                'location': 'Toronto, ON',
                'description': 'Design and implement ML models for healthcare applications.',
                'is_remote': False,
            },
            {
                'company_name': 'Finance Gurus',
                'job_title': 'Financial Analyst',
                'posting_url': 'https://financegurus.com/careers/financial-analyst',
                'location': 'New York, NY',
                'description': 'Provide financial insights and recommendations.',
                'is_remote': False,
            },
            {
                'company_name': 'E-Commerce Wizards',
                'job_title': 'UX Designer',
                'posting_url': 'https://ecommercewizards.com/careers/ux-designer',
                'location': 'Vancouver, BC',
                'description': 'Design user-friendly e-commerce platforms. Work closely with developers.',
                'is_remote': True,
            },
        ]

        # Create JobPostings
        for posting in mock_postings:
            JobPosting.objects.create(
                company_name=posting['company_name'],
                job_title=posting['job_title'],
                posting_url=posting['posting_url'],
                location=posting['location'],
                description=posting['description'],
                is_remote=posting['is_remote'],
                date_created=datetime.now()
            )
            self.stdout.write(self.style.SUCCESS(f"Successfully created job posting: {posting['job_title']} at {posting['company_name']}"))

        self.stdout.write(self.style.SUCCESS('5 mock job postings created successfully!'))
