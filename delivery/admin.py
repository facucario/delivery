from django.contrib import admin

from .models import Clients

admin.site.site_header = "Delivery"
admin.site.site_title = "Delivery"
admin.site.index_title = "Administración de Delivery"

class ClientsAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,          {'fields':['name','last_name','phone', 'email','last_visit','days_between_visits','special_visit']}),
        ('Dirección',   {'fields':['street_name','street_number','street_extra']}),
    ]

admin.site.register(Clients, ClientsAdmin)