# Generated by Django 5.0.6 on 2024-09-04 14:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_remove_program_college'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='program',
            name='university',
        ),
        migrations.DeleteModel(
            name='Eligibility',
        ),
        migrations.DeleteModel(
            name='Program',
        ),
        migrations.DeleteModel(
            name='University',
        ),
    ]
