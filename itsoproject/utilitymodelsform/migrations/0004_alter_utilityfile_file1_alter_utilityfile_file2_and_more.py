# Generated by Django 5.0.1 on 2024-01-03 11:19

import utilitymodelsform.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utilitymodelsform', '0003_remove_utilityfile_file_utilityfile_file1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='utilityfile',
            name='file1',
            field=models.FileField(blank=True, null=True, upload_to='utilitymodelfiles/', validators=[utilitymodelsform.models.validate_pdf]),
        ),
        migrations.AlterField(
            model_name='utilityfile',
            name='file2',
            field=models.FileField(blank=True, null=True, upload_to='utilitymodelfiles/', validators=[utilitymodelsform.models.validate_pdf]),
        ),
        migrations.AlterField(
            model_name='utilityfile',
            name='file3',
            field=models.FileField(blank=True, null=True, upload_to='utilitymodelfiles/', validators=[utilitymodelsform.models.validate_pdf]),
        ),
        migrations.AlterField(
            model_name='utilityfile',
            name='file4',
            field=models.FileField(blank=True, null=True, upload_to='utilitymodelfiles/', validators=[utilitymodelsform.models.validate_pdf]),
        ),
    ]
