# Generated by Django 3.0.9 on 2020-08-10 05:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tk', '0013_remove_ticket_group'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ticket',
            options={'ordering': ['-update'], 'verbose_name': 'Заявку', 'verbose_name_plural': 'Заявки'},
        ),
        migrations.AddField(
            model_name='ticket',
            name='date_close',
            field=models.DateTimeField(null=True, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='comment_master',
            field=models.TextField(default=' ', verbose_name='Комментарий'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='regions',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tk.Region', verbose_name='Район'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='street_only',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name=''),
        ),
    ]
