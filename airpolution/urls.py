from django.urls import path
from . import views

app_name ="airpolution"

urlpatterns = [
    path('', views.airpolution_welcome, name='welcome'),
]