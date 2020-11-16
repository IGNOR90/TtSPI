import django_filters
from .models import *


class TicketFilter(django_filters.FilterSet):
    class Meta:
        model = Ticket
        fields = ['id', 'regions', 'streets', 'home', 'flat', 'phone','author', 'master','viewticket' ,'tps_id','street_only']
        exclude = ['comment_mastera','coment','date', 'update', 'companylogin','logins','status']



class TicketCloseFilter(django_filters.FilterSet):
    class Meta:
        model = Ticket
        fields = ['id', 'regions', 'streets', 'home', 'flat', 'phone','author', 'master','viewticket' ,'tps_id','street_only','status']
        exclude = ['comment_mastera', 'coment','date', 'update', 'companylogin','logins']

class TicketFilterMaster(django_filters.FilterSet):
    class Meta:
        model = Ticket
        fields = ['id', 'regions', 'streets', 'home', 'flat', 'phone','author', 'viewticket', 'street_only','status']
        exclude = ['comment_mastera','coment','date', 'update', 'master','companylogin','logins']

