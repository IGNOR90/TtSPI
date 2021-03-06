# Generated by Django 3.0.8 on 2020-08-03 14:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tk', '0010_auto_20200803_1349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='coment',
            field=models.TextField(blank=True, default=' ', null=True, verbose_name='Комментарий'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='comment_master',
            field=models.TextField(blank=True, default=' ', null=True, verbose_name='Комментарий'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='companylogin',
            field=models.ForeignKey(default=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tk.Companylogin', verbose_name=''),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='flat',
            field=models.CharField(max_length=5, null=True, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='home',
            field=models.CharField(max_length=5, null=True, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='phone',
            field=models.CharField(max_length=20, null=True, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='priority',
            field=models.ForeignKey(default=2, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tk.Priority', verbose_name=''),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='tps_id',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name=''),
        ),
    ]
