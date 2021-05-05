from django.apps import AppConfig
from openwisp_controller.config.signals import device_registered
import types

class owMakeditConfig(AppConfig):
    name = 'ow-makedit'
    label = 'ow-makedit-config'
