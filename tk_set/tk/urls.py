from django.urls import path, include
from .views import *


urlpatterns = [
    path('', tk_list, name='tk_list'),
    path('add_ticket/', add_tk, name='add_tk'),


    # path('add_regions/', add_regions, name='add_regions'),

    path('ajax/load-cities/', load_cities, name='ajax_load_cities'),

    path('update_ticket/<str:pk>', update_tk, name='update_tk'),
    path('close_ticket/<str:pk>', close_tk, name='close_tk'),
    path('edit_ticket/<str:pk>', edit_tk, name='edit_tk'),
    path('delete_ticket/<str:pk>', delete_tk, name='delete_tk'),
    path('delete/<str:pk>', delete_comment, name='delete_comment'),
    path('about/<str:pk>', about, name='about'),
    path('region/', add_region, name='add_region'),
    path('street/', add_street, name='add_street'),
    path('master/', add_master, name='add_master'),
    path('user/', add_user, name='add_user'),
    path('ticket_close/', tk_list_close, name='tk_list_close'),
    path('login/', login_auth, name='login'),
    path('logout/', logout_view, name='logout'),
    path('export_csv/', export_csv, name='export_csv'),
    path('tk_export_csv/', ticket_export_csv, name='ticket_export_csv'),
    path('statistic/', statistic, name='statistic'),
]
