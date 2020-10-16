import datetime
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView

from .models import Clients


@login_required
def index(request):
    delta_time_zero = datetime.timedelta(days=0)
    clients_to_visit_list = []
    clients_visited_today = []
    clients_to_visit_tomorrow_list = []

    all_clients = Clients.objects.order_by('last_name')
    for client in all_clients:
        delta_time = datetime.timedelta(days=client.days_between_visits)
        if (datetime.date.today() == client.last_visit):
            clients_visited_today.append(client)
        if (((datetime.date.today()-client.last_visit)>=delta_time) and (client.special_visit is None or client.special_visit < datetime.date.today())) or (datetime.date.today() == client.special_visit):
            clients_to_visit_list.append(client)
        if ((((datetime.date.today()+datetime.timedelta(days=1)-client.last_visit)>=delta_time) and (client.special_visit is None or client.special_visit < datetime.date.today())) or (datetime.date.today()+datetime.timedelta(days=1) == client.special_visit)) and client not in clients_to_visit_list:
            clients_to_visit_tomorrow_list.append(client)

    context = {
        'clients_to_visit_list': clients_to_visit_list,
        'clients_visited_today': clients_visited_today,
        'clients_to_visit_tomorrow_list':clients_to_visit_tomorrow_list,
    }
    return render(request, 'delivery/index.html', context)

@login_required
def clients(request):
    all_clients_list = Clients.objects.order_by('last_name')
    context = {
        'all_clients_list': all_clients_list,
    }
    return render(request, 'delivery/all_clients.html', context)

@login_required
def client_details(request, client_id):
    client = get_object_or_404(Clients, pk=client_id)
    return render(request, 'delivery/client.html', {'client':client, })

def visited(request, client_id):
    if request.user.is_superuser:
        client = get_object_or_404(Clients, pk=client_id)
        if client:
            client.last_visit = datetime.date.today()
            client.special_visit = None
            client.save()
    return HttpResponseRedirect('/')

def snooze(request, client_id):
    if request.user.is_superuser:
        client = get_object_or_404(Clients, pk=client_id)
        if client:
            client.special_visit = datetime.date.today() + datetime.timedelta(days=1)
            client.save()
    return HttpResponseRedirect('/')

class ClientsCreateView(LoginRequiredMixin, CreateView):
    success_url = '/clients'
    model = Clients
    fields = ('name', 'last_name', 'street_name', 'street_number', 'street_extra', 'phone', 'email', 'days_between_visits')

class ClientsUpdate(LoginRequiredMixin, UpdateView):
    success_url = '/clients'
    model = Clients
    fields = ('name', 'last_name', 'street_name', 'street_number', 'street_extra', 'phone', 'email', 'days_between_visits')
    template_name_suffix = '_update_form'

class ClientsDelete(LoginRequiredMixin, DeleteView):
    success_url = '/clients'
    model = Clients