# Generated by Django 5.0.1 on 2024-02-10 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formupload', '0012_rename_uploadform_feedback_upload_form_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='feedback_text',
            field=models.TextField(blank=True, null=True),
        ),
    ]