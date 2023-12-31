# Generated by Django 5.0 on 2023-12-31 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='difficulty',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=3),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='review',
            name='useful',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=3),
            preserve_default=False,
        ),
    ]
