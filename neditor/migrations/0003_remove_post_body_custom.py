# Generated by Django 3.2.5 on 2022-11-11 13:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('neditor', '0002_auto_20221111_1921'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='body_custom',
        ),
    ]
