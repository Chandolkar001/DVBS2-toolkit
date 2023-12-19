# Generated by Django 5.0 on 2023-12-18 11:47

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_type', models.CharField(blank=True, default='pcap', max_length=20)),
                ('file', models.FileField(blank=True, null=True, upload_to=core.models.upload_to)),
                ('upload_date', models.DateField(blank=True, null=True)),
            ],
        ),
    ]
