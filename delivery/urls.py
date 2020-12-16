from django.urls import path
from django.conf.urls import url, include

from . import views

app_name = 'delivery'
urlpatterns = [
    url('', include('pwa.urls')),
    path('', views.index, name='index'),
    path('clients/', views.clients, name='all_clients'),
    path('clients/add/', views.ClientsCreateView.as_view(), name='add_clients'),
    path('clients/<int:client_id>/', views.client_details, name='details'),
    path('clients/<slug:pk>/edit/', views.ClientsUpdate.as_view(), name='edit_clients'),
    path('clients/<slug:pk>/delete/', views.ClientsDelete.as_view(), name='edit_clients'),
    path('clients/<int:client_id>/visited', views.visited, name='visited'),
    path('clients/<int:client_id>/snooze', views.snooze, name='snooze'),
]