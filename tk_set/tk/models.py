from django.db import models
from django.contrib.auth.models import User, Group
from datetime import datetime, timedelta
from django.utils.timezone import timezone
from django.core.exceptions import ValidationError
# from smart_selects.db_fields import ChainedForeignKey

# Create your models here.




class Region(models.Model):
    name = models.CharField(max_length = 200, null=True, verbose_name="")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Регион'
        verbose_name_plural = 'Регионы'


class Street(models.Model):
    name = models.CharField(max_length = 200, null=True, verbose_name="")
    region = models.ForeignKey(Region, null=True, on_delete=models.SET_NULL, verbose_name="", default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Улицу'
        verbose_name_plural = 'Улицы'


class Companylogin(models.Model):
    login = models.CharField(max_length = 200, null=True)

    def __str__(self):
        return self.login

    class Meta:
        verbose_name = 'Логин компании'
        verbose_name_plural = 'Логины компаний'


class ViewTicket(models.Model):
    name = models.CharField(max_length = 200, null=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Вид заявки'
        verbose_name_plural = 'Виды заявок'




class Priority(models.Model):
    name = models.CharField(max_length = 200, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Приоритет'
        verbose_name_plural = 'Приоритеты'

class Status(models.Model):
    name = models.CharField(max_length = 200, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'


class Master(models.Model):
    name = models.CharField(max_length = 200, null=True)
    master = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Мастера'
        verbose_name_plural = 'Мастера'


class Ticket(models.Model):
    date = models.DateTimeField(auto_now_add=True, null=True, verbose_name="")
    viewticket = models.ForeignKey(ViewTicket, null=True, on_delete=models.CASCADE, verbose_name="Вид заявки", default=True)
    master = models.ForeignKey(Master, null=True, on_delete=models.SET_NULL, verbose_name="Мастер", default=True)
    regions = models.ForeignKey(Region, null=True, on_delete=models.SET_NULL, verbose_name="Район")
    streets = models.ForeignKey(Street, blank=True, null=True, on_delete=models.SET_NULL, verbose_name="Улица")
    status = models.ForeignKey(Status, null=True, on_delete=models.SET_NULL, verbose_name="Статус", default=2)
    street_only = models.CharField(blank=True, max_length=100, null=True, verbose_name="")
    home = models.CharField(max_length = 5, null=True, verbose_name="")
    flat = models.CharField(blank=True, max_length = 5, null=True, verbose_name="")
    phone = models.CharField(max_length = 50, null=True, verbose_name="")
    companylogin = models.ForeignKey(Companylogin, null=True, on_delete=models.SET_NULL, verbose_name="", default=True)
    logins = models.CharField(blank=True,max_length = 15, null=True, verbose_name="")
    tps_id = models.CharField(blank=True, max_length=100, null=True, verbose_name="")
    priority = models.ForeignKey(Priority, null=True, on_delete=models.SET_NULL, verbose_name="", default=2)
    coment = models.TextField(blank=True,  null=True, verbose_name="Комментарий", default=" ")
    comment_master = models.TextField(verbose_name="Комментарий", default=" ")
    update = models.DateTimeField(auto_now=True)
    author = models.ForeignKey('auth.User', null=True, on_delete=models.SET_NULL, verbose_name="Автор", default=True)


    def __str__(self):
        return f'{[self.home, self.flat, self.phone]}'


    class Meta:
        verbose_name = 'Заявку'
        verbose_name_plural = 'Заявки'

        ordering = ['-update', ]


class Comment(models.Model):
    author = models.ForeignKey('auth.User', null=True, on_delete=models.SET_NULL, verbose_name="", default=True)
    text = models.CharField(max_length = 200, null=True, verbose_name="")
    date = models.DateTimeField(auto_now_add=True, null=True)
    post = models.ForeignKey(Ticket, null=True, on_delete=models.SET_NULL, verbose_name="", default=True)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'