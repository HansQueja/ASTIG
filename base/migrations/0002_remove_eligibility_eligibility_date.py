# Generated by Django 5.0.6 on 2024-09-04 13:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eligibility',
            name='eligibility_date',
        ),
    ]
