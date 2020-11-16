# coding: utf-8
import csv, os
from django.contrib import messages
from django.contrib.auth.models import User, Group
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from datetime import datetime, timedelta
from .forms import *
from .models import *
from .filters import *
from django.core.exceptions import ValidationError
from django.db.models import Q
from django.db.models import Count




@login_required(login_url='login')
def add_tk(request):
    tk = Ticket.objects.all().distinct()
    form = AddTkForm
    if request.method =='POST':
        form = AddTkForm(request.POST)
        if form.is_valid():
            logins = form.cleaned_data["logins"]
            tps_id = form.cleaned_data["tps_id"]
            coment = form.cleaned_data["coment"]
            priority = form.cleaned_data["priority"]


            # if form.cleaned_data["street_only"] and form.cleaned_data["regions"] and form.cleaned_data["home"] and form.cleaned_data["phone"] and (form.cleaned_data["flat"] or form.cleaned_data["flat"] == None) and (form.cleaned_data["tps_id"] or form.cleaned_data["tps_id"] == None) and (form.cleaned_data["logins"] or form.cleaned_data["logins"] == None):
            if form.cleaned_data["street_only"] and form.cleaned_data["regions"] and form.cleaned_data["home"] and form.cleaned_data["phone"] and (form.cleaned_data["flat"] or form.cleaned_data["flat"]== None) and (form.cleaned_data["tps_id"] or form.cleaned_data["tps_id"] == None):
            # if form.cleaned_data["street_only"] and form.cleaned_data["regions"] and form.cleaned_data["home"] and form.cleaned_data["phone"] or form.cleaned_data["street_only"] and form.cleaned_data["regions"] and form.cleaned_data["home"] and form.cleaned_data["phone"] and form.cleaned_data["flat"]:
                get_tk, create_tk = Ticket.objects.get_or_create(
                    regions=form.cleaned_data["regions"],
                    street_only=form.cleaned_data["street_only"],
                    flat=form.cleaned_data["flat"],
                    home=form.cleaned_data["home"],
                    phone=form.cleaned_data["phone"],
                    logins=form.cleaned_data["logins"],
                    tps_id=form.cleaned_data["tps_id"],
                    coment=form.cleaned_data["coment"],
                    priority = form.cleaned_data["priority"],
                    status_id=2,
                )
                if not create_tk:
                    raise ValidationError("такая заявка уже существует")
                else:
                    # raise ValidationError("такая заявка уже существует")
                    messages.info(request, 'Заявка добавлена')
                    return redirect('/')
            # elif form.cleaned_data["streets"] and form.cleaned_data["regions"] and form.cleaned_data["home"] and form.cleaned_data["phone"] and form.cleaned_data["flat"] and (form.cleaned_data["tps_id"] or form.cleaned_data["tps_id"] == None) and (form.cleaned_data["logins"] or form.cleaned_data["logins"] == None):
            elif form.cleaned_data["streets"] and form.cleaned_data["regions"] and form.cleaned_data["home"] and form.cleaned_data["phone"] and (form.cleaned_data["flat"] or form.cleaned_data["flat"]== None) and (form.cleaned_data["tps_id"] or form.cleaned_data["tps_id"] == None):
            # elif form.cleaned_data["streets"] and form.cleaned_data["regions"] and form.cleaned_data["home"] and form.cleaned_data["phone"] or form.cleaned_data["streets"] and form.cleaned_data["regions"] and \
            #          form.cleaned_data["home"] and form.cleaned_data["phone"] and form.cleaned_data["flat"]:
                get_tk, create_tk = Ticket.objects.get_or_create(
                    regions=form.cleaned_data["regions"],
                    streets=form.cleaned_data["streets"],
                    flat=form.cleaned_data["flat"],
                    home=form.cleaned_data["home"],
                    phone=form.cleaned_data["phone"],
                    logins=form.cleaned_data["logins"],
                    tps_id = form.cleaned_data["tps_id"],
                    coment = form.cleaned_data["coment"],
                    priority = form.cleaned_data["priority"],
                    status_id=2,
                )
                if not create_tk:
                    raise ValidationError("такая заявка уже существует")
                else:
                    messages.info(request, 'Заявка добавлена')
            return redirect('/')
    context = {'form':form, 'tk': tk}
    return render(request, 'tk/add_tk.html', context)

def load_cities(request):
    region_id = request.GET.get('region')
    streets = Street.objects.filter(region_id=region_id).order_by('name')
    return render(request, 'tk/city_dropdown_list_options.html', {'streets': streets})


# def add_tk(request):
#     form = AddTkForm
#     if request.method=='POST':
#         form = AddTkForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/')
#     context = {'form':form}
#     return render(request, 'tk/add_tk.html', context)



@login_required(login_url='login')
def update_tk(request, pk):
    tk = Ticket.objects.get(id=pk)
    form = UpdateTkForm(instance=tk)
    if request.method=='POST':
        form = UpdateTkForm(request.POST, instance=tk)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form':form}
    return render(request, 'tk/update_tk.html', context)

@login_required(login_url='login')
def close_tk(request, pk):
    tk = Ticket.objects.get(id=pk)
    form = CloseTkForm(instance=tk)
    if request.method=='POST':
        form = CloseTkForm(request.POST, instance=tk)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form':form, 'tk':tk}
    return render(request, 'tk/close_tk.html', context)


@login_required(login_url='login')
def edit_tk(request, pk):
    tk = Ticket.objects.get(id=pk)
    form = EditMasterTkForm(instance=tk)
    if request.method=='POST':
        form = EditMasterTkForm(request.POST, instance=tk)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form':form, 'tk':tk}
    return render(request, 'tk/edit_master_tk.html', context)


@login_required(login_url='login')
def tk_list(request):

    if request.user.is_superuser or request.user.is_staff:

        tk = Ticket.objects.filter(status=2)
        tkFilter = TicketFilter(request.GET, queryset=tk)
        counts = tk.filter().count()
        count_tps = Ticket.objects.filter(tps_id__isnull=False, status=2).count()
        count_sp = Ticket.objects.filter(tps_id__isnull=True, status=2).count()

        context = {
            'tk': tk,
            'counts': counts,
            'count_tps': count_tps,
            'tkFilter':tkFilter,
            'count_sp':count_sp
        }
    else:
        user = Master.objects.get(master=request.user.id)
        master_tk = Ticket.objects.filter(master=user, status=2)
        tkFilter_m = TicketFilterMaster(request.GET, queryset=master_tk)
        counts = master_tk.filter().count()
        count_tps = Ticket.objects.filter(tps_id__isnull=False, master=user, status=2).count()
        count_sp = Ticket.objects.filter(tps_id__isnull=True, master=user, status=2).count()

        context = {
            'master_tk': master_tk,
            'counts': counts,
            'count_tps': count_tps,
            'tkFilter_m': tkFilter_m,
            'count_sp': count_sp
        }
    return render(request, 'tk/tklist.html', context)
#Ограничивает вход на страницу где его нет, там всё можно
@login_required(login_url='login')
def tk_list_close(request):



    if request.user.is_superuser or request.user.is_staff:

        tk = Ticket.objects.all()
        tkFilter = TicketCloseFilter(request.GET, queryset=tk)
        counts = tk.filter().count()
        count_tps = Ticket.objects.filter(tps_id__isnull=False).count

        context = {
            'tk': tk,
            'counts': counts,
            'count_tps': count_tps,
            'tkFilter':tkFilter,

        }
        return render(request, 'tk/tklistm.html', context)

    else:
        user = Master.objects.get(master=request.user.id)
        tk = Ticket.objects.filter(master=user)
        tkFilter = TicketFilterMaster(request.GET, queryset=tk)
        counts = tk.filter().count()
        count_tps = Ticket.objects.filter(tps_id__isnull=False).count

        context = {
            'tk': tk,
            'counts': counts,
            'count_tps': count_tps,
            'tkFilter': tkFilter,
        }
        return render(request, 'tk/tklistm.html', context)



def login_auth(request):
    context = {}
    if request.user.is_authenticated:
        return redirect('tk_list')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('tk_list')
            else:
                messages.info(request, 'Не верный логин или пароль')


        return render(request, 'tk/login.html', context)

#
#
#


def logout_view(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def add_region(request):
    region = Region.objects.all()
    form = AddRegionForm
    if request.method=='POST':
        form = AddRegionForm(request.POST)
        if form.is_valid():
            get_region, create_region = Region.objects.get_or_create(
                name=form.cleaned_data["name"],
            )
            if not create_region:
                raise ValidationError("такой район уже существует")
            else:
                return redirect('add_region')
    context = {'form':form, 'region': region}
    return render(request, 'tk/add_region.html', context)

@login_required(login_url='login')
def add_street(request):
    street = Street.objects.all()

    context_list = []
    get_all_street = Region.objects.all()
    for cat in get_all_street:
        get_street_in_region = Street.objects.filter(region=cat.pk).values()
        context = {"id": cat.pk, "cat_name": cat.name, 'street': get_street_in_region}
        context_list.append(context)


    form = AddStreetForm
    if request.method=='POST':
        form = AddStreetForm(request.POST)
        if form.is_valid():
            get_region = Region.objects.get(name=form.cleaned_data["region"])
            get_street, create_street = Street.objects.get_or_create(
                name=form.cleaned_data["name"],
                region_id=get_region.id,
            )
            if not create_street:
                raise ValidationError("такая улица уже существует")
            else:
                return redirect('add_street')
    context = {'form':form, 'street': street,'context': context_list}
    return render(request, 'tk/add_street.html', context)





@login_required(login_url='login')
def delete_tk(request,pk=None):
    post = Ticket.objects.get(id=pk)
    post.delete()
    return redirect('/')


# def time(request, self):
#
#         return render(request, 'tk/tklist.html', context)

@login_required(login_url='login')
def about(request, pk):
    post = get_object_or_404(Ticket, id=pk)
    comment = Comment.objects.filter(post=post)
    if request.method == 'POST':
        form = PostCommentForm(request.POST)
        if form.is_valid():
            comn = form.save(commit=True)
            comn.post = post
            comn.save()
            form = PostCommentForm()

    else:
        form = PostCommentForm()
    tk = Ticket.objects.get(id=pk)
    context = {
        'tk':tk,
        'comment': comment,
        'form': form,
        'post': post,
    }
    return render(request, 'tk/about.html', context)

# def delete_comment(request, comment_pk):
#     obj = get_object_or_404(Ticket, pk=comment_pk)
#     success_url = redirect('appname:about', pk=obj.task.pk)
#     Comment.objects.filter(pk=obj.pk).delete()
#     return success_url


@login_required(login_url='login')
def delete_comment(request,pk=None,):
    post = Comment.objects.get(id=pk)
    post.delete()
    return redirect('/')


@login_required(login_url='login')
def add_master(request):

    master = Master.objects.all()
    form = AddMasterForm
    if request.method=='POST':
        form = AddMasterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_master')
    context = {'form':form, 'master': master}
    return render(request, 'tk/add_master.html', context)

@login_required(login_url='login')
def add_user(request):
    group = Group.objects.all()
    user = User.objects.all()




    form = CreateUserForm
    if request.method=='POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_user')
    context = {'user': user, 'form':form, 'group':group}
    return render(request, 'tk/add_user.html', context)

@login_required(login_url='login')
def export_csv(request):
    response = open(os.path.expanduser('~/streets.csv'), 'wb')
    response.write(u'\ufeff'.encode('utf8'))

    response = HttpResponse(content_type='text/csv; charset=windows-1251')

    writer = csv.writer(response, delimiter=';', dialect='excel')
    writer.writerow(['Имя', 'Район'])

    for streets in Street.objects.all().values('name', 'region'):
        get_region = Region.objects.get(pk=streets.get('region'))
        streets['region'] = get_region.name
        print(streets)
        writer.writerow([streets.get('name'), streets.get('region')])


    response['Content-Disposition'] = 'attachment; filename="streets.csv"'

    return response

@login_required(login_url='login')
def ticket_export_csv(request):
    user = Master.objects.get(id=request.user.id)
    response = open(os.path.expanduser('~/ticket.csv'), 'wb')
    response.write(u'\ufeff'.encode('utf8'))

    response = HttpResponse(content_type='text/csv; charset=windows-1251')

    writer = csv.writer(response, delimiter=';', dialect='excel')
    writer.writerow(['Дата','Район', 'Улица', 'Улица','Дом', 'Квартира', 'Телефон', 'Оператор','Вид заявки', 'Комментарий'])
    response.close()


    for ticket in Ticket.objects.filter(status=2, master=user).values('date', 'regions','streets__name', 'street_only', 'home', 'flat', 'phone','author', 'viewticket', 'coment'):
        get_viewticket = ViewTicket.objects.get(id=ticket.get('viewticket'))
        get_region = Region.objects.get(pk=ticket.get('regions'))
        # get_street = Street.objects.get(id=ticket.get('regions'))
        get_author = User.objects.get(id=ticket.get('author'))


        ticket['regions'] = get_region.name
        # ticket['street'] = get_street.name
        ticket['author'] = get_author.first_name
        ticket['viewticket'] = get_viewticket.name

        writer.writerow([ticket.get('date'), ticket.get('regions'), ticket.get('streets__name'), ticket.get('street_only'), ticket.get('home'), ticket.get('flat'), ticket.get('phone'), ticket.get('author'), ticket.get('viewticket'), ticket.get('coment')])



    response['Content-Disposition'] = 'attachment; filename="ticket.csv"'

    return response


@login_required(login_url='login')
def statistic(request):
    counts = Ticket.objects.filter(status=2).count()
    count_tps = Ticket.objects.filter(tps_id__isnull=False, status=2).count()
    count_sp = Ticket.objects.filter(tps_id__isnull=True, status=2).count()
    count_ust = Ticket.objects.filter(viewticket=2, status=2).count()
    count_rem = Ticket.objects.filter(viewticket=1, status=2).count()
    count_close = Ticket.objects.filter(~Q(status=2)).count()
    # user_posts = Ticket.objects.annotate(Count('master'))
    context = {
        'counts': counts,
        'count_tps': count_tps,
        'count_sp': count_sp,
        'count_ust':count_ust,
        'count_rem':count_rem,
        'count_close':count_close,
        # 'user_posts':user_posts,

    }
    return render(request, 'tk/statistic.html', context)


#
# def handler500(request):
#     response = render_to_response('500.html', {},
#                                   context_instance=RequestContext(request))
#     response.status_code = 500
#     return response