# Generated by Django 4.2.5 on 2023-10-01 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('file_hosting_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filemodel',
            name='file',
            field=models.FileField(unique=True, upload_to='uploaded'),
        ),
    ]