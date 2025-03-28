# Generated by Django 5.1.4 on 2024-12-16 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0002_rename_entry_timetable_alter_timetable_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timetable',
            name='location',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='subject_type',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='teacher',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
