# tracker/management/commands/create_mock_documents.py
from django.core.management.base import BaseCommand
from tracker.models import Document
from django.utils import timezone
import os

class Command(BaseCommand):
    help = 'Create mock documents'

    def handle(self, *args, **kwargs):
        mock_documents = [
            {
                'document_type': 'resume',
                'document_name': 'John Doe Resume',
                'file': 'https://example.com/resume/johndoe.pdf',
                'text_content': 'John Doe Resume Content',
                'date_uploaded': timezone.now()
            },
            {
                'document_type': 'cover_letter',
                'document_name': 'John Doe Cover Letter',
                'file': 'https://example.com/cover_letter/johndoe.pdf',
                'text_content': 'John Doe Cover Letter Content',
                'date_uploaded': timezone.now()
            },
            {
                'document_type': 'other',
                'document_name': 'John Doe Portfolio',
                'file': 'https://example.com/portfolio/johndoe.pdf',
                'text_content': 'John Doe Portfolio Content',
                'date_uploaded': timezone.now()
            },
            {
                'document_type': 'resume',
                'document_name': 'Jane Smith Resume',
                'file': 'https://example.com/resume/janesmith.pdf',
                'text_content': 'Jane Smith Resume Content',
                'date_uploaded': timezone.now()
            },
            {
                'document_type': 'cover_letter',
                'document_name': 'Jane Smith Cover Letter',
                'file': 'https://example.com/cover_letter/janesmith.pdf',
                'text_content': 'Jane Smith Cover Letter Content',
                'date_uploaded': timezone.now()
            },
        ]

        for doc in mock_documents:
            Document.objects.create(
                document_type=doc['document_type'],
                document_name=doc['document_name'],
                file=doc['file'],
                text_content=doc['text_content'],
                date_uploaded=doc['date_uploaded']
            )

        self.stdout.write(self.style.SUCCESS('Successfully created mock documents'))