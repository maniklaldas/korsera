# Generated by Django 3.1.4 on 2021-01-15 06:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0008_course_teaching_assistant'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='structure',
        ),
    ]
