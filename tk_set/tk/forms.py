from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django import forms
from .models import *


# class AddTicketForm(forms.Form):
#     viewticket = forms.ModelChoiceField(label='', empty_label='Вид заявки', queryset=ViewTicket.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
#     master = forms.ModelChoiceField(label='',empty_label='Выберите мастера', queryset=Master.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
#     regions = forms.ModelChoiceField(label='',empty_label='Выберите район', queryset=Region.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
#     streets = forms.ModelChoiceField(label='',empty_label='Выберите улицу', queryset=Street.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
#     street_only = forms.CharField(required=False, label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Альтернативная улица'}))
#     home = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Дом'}))
#     flat = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Кв'}))
#     phone = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Телефон'}))
#     companylogin = forms.ModelChoiceField(label='',empty_label='логин', queryset=Companylogin.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
#     logins = forms.IntegerField(label='', widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Логин'}))
#     priority = forms.ModelChoiceField(label='', empty_label='Выберите приоритет', queryset=Priority.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
#     comment = forms.CharField(required=False, label='', widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Комментарий'}))
#     class Meta:
#         model = Ticket
#         fields = ['viewticket', 'master', 'regions', 'streets', 'street_only', 'home', 'flat', 'phone', 'companylogin', 'logins', 'priority', 'comment']

class AddRegionForm(ModelForm):
    class Meta:
        model = Region
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите название района'}),
        }


class AddStreetForm(ModelForm):
    class Meta:
        model = Street
        fields = '__all__'
        widgets = {
        'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите название улицы'}),
        'region': forms.Select(attrs={'class': 'form-control'}),
        }



# class AddTkForm(forms.ModelForm):
#     class Meta:
#         model = Ticket
#         fields = '__all__'
#         exclude = ['author', 'comment_master', 'status']
#
#         widgets = {
#             'home': forms.TextInput(attrs={'class': 'col-md-2 form', 'placeholder': 'Дом'}),
#             'flat': forms.TextInput(attrs={'class': 'form col-md-2', 'placeholder': 'Кв'}),
#             'phone': forms.TextInput(attrs={'class': 'form col-md-2', 'placeholder': 'Телефон'}),
#             'logins': forms.TextInput(attrs={'class': 'form col-md-2', 'placeholder': 'Логин'}),
#             'tps_id': forms.TextInput(attrs={'class': 'form col-md-4', 'placeholder': 'ID тикета с TPS'}),
#             'street_only': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Альтернативная улица'}),
#             'coment': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Комментарий', 'row': 3}),
#             'comment_master': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Комментарий мастера', 'row': 3}),
#             'viewticket': forms.Select(attrs={'class': 'form-control'}),
#             'master': forms.Select(attrs={'class': 'form-control'}),
#             'regions': forms.Select(attrs={'class': 'form-control'}),
#             'streets': forms.Select(attrs={'class': 'form-control'}),
#             'status': forms.Select(attrs={'class': 'form-control'}),
#             'companylogin': forms.Select(attrs={'class': 'form col-md-2'}),
#             'priority': forms.RadioSelect(attrs={'class': 'radio'}),
#
#         }

# ['status','coment', 'home', 'flat', 'phone', 'logins', 'tps_id', 'street_only', 'viewticket', 'master', 'regions', 'streets', 'companylogin', 'priority']



class CloseTkForm(ModelForm):
    class Meta:
        model = Ticket
        fields = ['status', 'comment_master']
        exclude = ['author']

        widgets = {
            'comment_master': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Комментарий', 'row': 3}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }

class EditMasterTkForm(ModelForm):
    class Meta:
        model = Ticket
        fields = ['master']
        exclude = ['author']

        widgets = {
            'master': forms.Select(attrs={'class': 'form-control'}),
        }


class PostCommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
        'text': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ваш текст'}),
        }


class AddMasterForm(ModelForm):
    class Meta:
        model = Master
        fields = '__all__'
        widgets = {
        'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите имя мастера'}),
        'master': forms.Select(attrs={'class': 'form-control'}),
        }

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'first_name']

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите логин'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите имя'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Пароль'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Повторите пароль'}),

        }
        # widgets = {
        # 'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите имя мастера'}),
        # 'master': forms.Select(attrs={'class': 'form-control'}),
        # }


class AddTkForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = '__all__'
        exclude = ['author', 'comment_master', 'status']

        widgets = {
            'home': forms.TextInput(attrs={'class': 'col-md-2 form', 'placeholder': 'Дом'}),
            'flat': forms.TextInput(attrs={'class': 'form col-md-2', 'placeholder': 'Кв'}),
            'phone': forms.TextInput(attrs={'class': 'form col-md-2', 'placeholder': 'Телефон'}),
            'logins': forms.TextInput(attrs={'class': 'form col-md-2', 'placeholder': 'Логин'}),
            'tps_id': forms.TextInput(attrs={'class': 'form col-md-4', 'placeholder': 'ID тикета с TPS'}),
            'street_only': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Альтернативная улица'}),
            'coment': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Комментарий', 'row': 3}),
            'comment_master': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Комментарий мастера', 'row': 3}),
            'viewticket': forms.Select(attrs={'class': 'form-control'}),
            'master': forms.Select(attrs={'class': 'form-control'}),
            'regions': forms.Select(attrs={'class': 'form-control'}),
            'streets': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'companylogin': forms.Select(attrs={'class': 'form col-md-2'}),
            'priority': forms.RadioSelect(attrs={'class': 'radio'}),

        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['streets'].queryset = Street.objects.none()

        if 'regions' in self.data:
            try:
                region_id = int(self.data.get('regions'))
                self.fields['streets'].queryset = Street.objects.filter(region_id=region_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['streets'].queryset = self.instance.regions.street_set.order_by('name')



class UpdateTkForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = '__all__'
        exclude = ['author', 'comment_master']

        widgets = {
            'home': forms.TextInput(attrs={'class': 'col-md-2 form', 'placeholder': 'Дом'}),
            'flat': forms.TextInput(attrs={'class': 'form col-md-2', 'placeholder': 'Кв'}),
            'phone': forms.TextInput(attrs={'class': 'form col-md-2', 'placeholder': 'Телефон'}),
            'logins': forms.TextInput(attrs={'class': 'form col-md-2', 'placeholder': 'Логин'}),
            'tps_id': forms.TextInput(attrs={'class': 'form col-md-4', 'placeholder': 'ID тикета с TPS'}),
            'street_only': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Альтернативная улица'}),
            'coment': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Комментарий', 'row': 3}),
            'comment_master': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Комментарий мастера', 'row': 3}),
            'viewticket': forms.Select(attrs={'class': 'form-control'}),
            'master': forms.Select(attrs={'class': 'form-control'}),
            'regions': forms.Select(attrs={'class': 'form-control'}),
            'streets': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'companylogin': forms.Select(attrs={'class': 'form col-md-2'}),
            'priority': forms.RadioSelect(attrs={'class': 'radio'}),

        }