# Generated by Django 4.1.1 on 2023-05-31 13:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_applicant'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='applicant',
            name='cv',
        ),
    ]
