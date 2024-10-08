# Generated by Django 4.2.16 on 2024-09-26 13:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobapplication',
            name='company_name',
        ),
        migrations.RemoveField(
            model_name='jobapplication',
            name='job_url',
        ),
        migrations.RemoveField(
            model_name='jobapplication',
            name='position',
        ),
        migrations.AddField(
            model_name='jobapplication',
            name='additional_documents',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='additional_documents', to='tracker.document'),
        ),
        migrations.AddField(
            model_name='jobapplication',
            name='job_posting',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='application', to='tracker.jobposting'),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='cover_letter',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='cover_letters', to='tracker.document'),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='notes',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='resume',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='resumes', to='tracker.document'),
        ),
    ]
