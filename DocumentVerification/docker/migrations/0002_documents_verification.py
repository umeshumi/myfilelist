# Generated by Django 2.1.3 on 2018-12-29 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docker', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='documents',
            name='Verification',
            field=models.BooleanField(default=False),
        ),
    ]