# Generated by Django 5.2.3 on 2025-06-25 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0012_apply_job'),
    ]

    operations = [
        migrations.AddField(
            model_name='apply',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
