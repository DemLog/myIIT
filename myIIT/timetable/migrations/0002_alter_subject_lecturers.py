# Generated by Django 3.2.6 on 2021-11-11 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='lecturers',
            field=models.ManyToManyField(to='timetable.Lecturer', verbose_name='Преподаватели'),
        ),
    ]
