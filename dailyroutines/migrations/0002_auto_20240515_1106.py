# Generated by Django 3.2.25 on 2024-05-15 11:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dailyroutines', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dailyroutine',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dailyroutine',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
