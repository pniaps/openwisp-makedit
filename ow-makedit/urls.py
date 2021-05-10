from django.urls import path
from . import views

urlpatterns = [
    path('status/<path:device_id>', views.device_status, name='mk-device-status'),
    path('devices', views.devices, name='mk-devices'),
]