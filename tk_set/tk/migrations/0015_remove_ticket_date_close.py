# Generated by Django 3.0.9 on 2020-08-10 05:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tk', '0014_auto_20200810_1035'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='date_close',
        ),
    ]