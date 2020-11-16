from django.contrib import admin
from .models import *

# Register your models here.


class TicketAdmin(admin.ModelAdmin):
    list_display = ('date', 'update', 'street_only', 'home', 'flat', 'phone', 'coment', 'tps_id')
    search_fields = ('street_only', 'home', 'flat', 'phone', 'tps_id')

admin.site.register(Ticket, TicketAdmin)
admin.site.register(Region)
admin.site.register(Street)
admin.site.register(Companylogin)
admin.site.register(ViewTicket)
admin.site.register(Comment)
admin.site.register(Priority)
admin.site.register(Status)
admin.site.register(Master)


