# Generated by Django 3.0.8 on 2020-07-31 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tk', '0004_auto_20200801_0046'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='tps_id',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.CharField(max_length=200, null=True, verbose_name=''),
        ),
    ]