# Generated by Django 5.0.2 on 2025-03-05 17:30

import results.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LabResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result_number', models.CharField(max_length=50, unique=True)),
                ('patient_name', models.CharField(max_length=255)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('result_image', models.ImageField(upload_to='results/')),
                ('password', models.CharField(default=results.models.generate_random_password, max_length=6)),
                ('qr_code', models.ImageField(blank=True, upload_to='qr_codes/')),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
    ]
