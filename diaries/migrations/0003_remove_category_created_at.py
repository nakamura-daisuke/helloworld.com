# Generated by Django 3.0.4 on 2020-04-17 06:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diaries', '0002_category_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='created_at',
        ),
    ]