# Generated by Django 5.1.4 on 2024-12-15 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NewsApp', '0002_new_colour'),
    ]

    operations = [
        migrations.AddField(
            model_name='new',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='img\\'),
        ),
    ]