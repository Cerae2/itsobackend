# Generated by Django 5.0.1 on 2024-02-03 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formupload', '0004_remove_fileuploads_file2_remove_fileuploads_file3_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file1', models.FileField(upload_to='uploads/')),
            ],
        ),
        migrations.RemoveField(
            model_name='fileuploads',
            name='file1',
        ),
        migrations.AddField(
            model_name='fileuploads',
            name='file3',
            field=models.ManyToManyField(to='formupload.publication'),
        ),
    ]
