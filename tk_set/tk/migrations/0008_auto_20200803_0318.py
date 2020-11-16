# Generated by Django 3.0.8 on 2020-08-02 22:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tk', '0007_ticket_update'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='status',
            field=models.ForeignKey(default=2, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tk.Status', verbose_name='Район'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='author',
            field=models.ForeignKey(default=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='coment',
            field=models.TextField(blank=True, null=True, verbose_name='Комментарий'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='companylogin',
            field=models.ForeignKey(default=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tk.Companylogin', verbose_name='Логин'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='flat',
            field=models.CharField(max_length=5, null=True, verbose_name='Кв'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='home',
            field=models.CharField(max_length=5, null=True, verbose_name='Дом'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='master',
            field=models.ForeignKey(default=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tk.Master', verbose_name='Мастер'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='phone',
            field=models.CharField(max_length=20, null=True, verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='priority',
            field=models.ForeignKey(default=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tk.Priority', verbose_name='Приоритет'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='regions',
            field=models.ForeignKey(default=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tk.Region', verbose_name='Район'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='street_only',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Альтернативная улица'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='streets',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tk.Street', verbose_name='Улица'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='tps_id',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Tps ID'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='viewticket',
            field=models.ForeignKey(default=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tk.ViewTicket', verbose_name='Вид заявки'),
        ),
    ]
