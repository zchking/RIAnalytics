# Generated by Django 4.0 on 2022-05-14 02:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('text_analytics', '0002_alter_textanalyticsmodel_keyword_file_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='textanalyticsmodel',
            old_name='report_file',
            new_name='report_files',
        ),
    ]