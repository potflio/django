# Generated by Django 5.0.3 on 2025-04-08 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='hobbies',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
