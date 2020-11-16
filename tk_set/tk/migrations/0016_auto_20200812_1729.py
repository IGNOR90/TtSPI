# Generated by Django 3.0.9 on 2020-08-12 12:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tk', '0015_remove_ticket_date_close'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='streets',
            field=models.ForeignKey(blank=True, default='Нет', null=True, on_delete=django.db.models.deletion.SET_NULL, to='tk.Street', verbose_name='Улица'),
        ),
    ]