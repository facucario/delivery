from django.db import models
import datetime

# Model for Clients.
class Clients(models.Model):
    name = models.CharField(max_length=200, blank=True, verbose_name='Nombre')
    last_name = models.CharField(max_length=200, verbose_name='Apellido')
    street_name = models.CharField(max_length=200, verbose_name='Calle')
    street_number = models.CharField(max_length=200, verbose_name='Número')
    street_extra = models.CharField(max_length=200, blank=True, verbose_name='Indicaciones')
    phone = models.PositiveIntegerField(verbose_name='Teléfono')
    email = models.EmailField(blank=True, verbose_name='Email')
    days_between_visits = models.PositiveIntegerField(default=7, verbose_name='Días entre visitas')
    registered = models.DateField(default=datetime.date.today, verbose_name='Fecha de alta')
    last_visit = models.DateField(default=datetime.date.today, verbose_name='Última visita')
    special_visit = models.DateField(null=True, blank=True, verbose_name='Visita especial')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'cliente'