from django.apps import AppConfig
from openwisp_controller.config.signals import device_registered
import types

class owMakeditConfig(AppConfig):
    name = 'ow-makedit'
    label = 'ow-makedit-config'

    def ready(self, *args, **kwargs):
        self.replace_device_get_context()

    def replace_device_get_context(self):
        from openwisp_controller.config.models import Config
        _orig_config_context = Config.get_context
        def config_get_context(self, system=False):
            context = _orig_config_context(self, system)
            if self._has_device():
                context['mac_suffix'] = self.mac_address[9:11]+self.mac_address[12:14]+self.mac_address[15:17]
            return context
        Config.get_context = config_get_context

