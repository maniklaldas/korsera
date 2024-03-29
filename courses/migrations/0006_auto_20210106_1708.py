# Generated by Django 3.1.4 on 2021-01-06 11:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20210105_1721'),
        ('courses', '0005_auto_20210106_1706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='banner_image1',
            field=models.ImageField(blank=True, default='default_course.png', null=True, upload_to='media/course_images'),
        ),
        migrations.AlterField(
            model_name='course',
            name='banner_image2',
            field=models.ImageField(blank=True, default='default_course.png', null=True, upload_to='media/course_images'),
        ),
        migrations.AlterField(
            model_name='course',
            name='instructor2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='instructor2', to='accounts.instructor'),
        ),
    ]
