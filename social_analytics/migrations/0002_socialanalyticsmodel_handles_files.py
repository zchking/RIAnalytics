# Generated by Django 3.2 on 2022-06-08 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social_analytics', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='socialanalyticsmodel',
            name='handles_files',
            field=models.FileField(blank=True, upload_to='files/'),
        ),
    ]
