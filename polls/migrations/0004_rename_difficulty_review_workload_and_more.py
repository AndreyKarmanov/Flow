# Generated by Django 5.0.1 on 2024-01-14 00:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_school_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='difficulty',
            new_name='workload',
        ),
        migrations.RemoveField(
            model_name='course',
            name='extra',
        ),
        migrations.RemoveField(
            model_name='course',
            name='lastUpdated',
        ),
        migrations.RemoveField(
            model_name='course',
            name='url',
        ),
    ]
