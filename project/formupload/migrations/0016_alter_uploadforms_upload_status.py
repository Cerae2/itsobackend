# Generated by Django 5.0.1 on 2024-02-10 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formupload', '0015_alter_uploadforms_form_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadforms',
            name='upload_status',
            field=models.CharField(blank=True, default='Pending', max_length=50, null=True),
        ),
    ]
