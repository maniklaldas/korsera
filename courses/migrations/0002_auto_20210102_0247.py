# Generated by Django 3.1.4 on 2021-01-01 21:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20210102_0247'),
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='current_batch',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='course',
            name='department',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='course',
            name='course_id',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.CreateModel(
            name='EnrolledStudent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reg_no', models.CharField(max_length=20, unique=True)),
                ('batch', models.CharField(default='', max_length=10)),
                ('status', models.CharField(choices=[('T', 'Pursuing'), ('P', 'Passed'), ('F', 'Failed'), ('W', 'Withdrawn'), ('D', 'Deregistered')], max_length=15)),
                ('grade', models.DecimalField(decimal_places=2, default=0.0, max_digits=4)),
                ('remarks', models.TextField(default='', max_length=2000)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course', to='courses.course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student', to='accounts.student')),
            ],
        ),
    ]
