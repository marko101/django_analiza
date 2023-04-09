from django.contrib import admin
from airpolution.models import Country, Polutant, PolutantEntry

# Register your models here.
admin.site.register(Country)
admin.site.register(Polutant)
admin.site.register(PolutantEntry)
