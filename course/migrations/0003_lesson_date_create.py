# Generated by Django 5.0.1 on 2024-06-30 16:45

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='date_create',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='lesson create date'),
            preserve_default=False,
        ),
    ]
