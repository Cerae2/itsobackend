# Generated by Django 5.0.1 on 2024-02-10 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formupload', '0014_alter_uploadforms_upload_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadforms',
            name='form_type',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]