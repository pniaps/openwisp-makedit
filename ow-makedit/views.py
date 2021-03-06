import uuid
from datetime import datetime
from dateutil.relativedelta import relativedelta
from django.shortcuts import render
from openwisp_controller.config.models import Device
from swapper import load_model

from openwisp_controller.config.models import Device
DeviceData = load_model('device_monitoring', 'DeviceData')


def device_status(request, device_id):
    device = Device.objects.get(pk=device_id)
    device_data = DeviceData(pk=uuid.UUID(device_id))

    if(device_data.data):
        measured_at = datetime.strptime(device_data.data_timestamp[0:19], '%Y-%m-%dT%H:%M:%S')
        time_elapsed = int((datetime.utcnow() - measured_at).total_seconds())
        if 'general' in device_data.data and 'uptime' in device_data.data['general']:
            delta = relativedelta(seconds=device_data.data['general']['uptime'] + time_elapsed)
            uptime = {
                'days': '{0.days}'.format(delta),
                'hours': '{0.hours}'.format(delta),
                'minutes': '{0.minutes}'.format(delta),
                'seconds': '{0.seconds}'.format(delta)
            }
        clients = []
        for interface in device_data.data.get('interfaces', []):
            if 'wireless' in interface and 'clients' in interface['wireless']:
                for client in interface['wireless']['clients']:
                    interface['wireless']['frequency'] /= 1000
                    clients.append({
                        'mac': client['mac'],
                        'vendor': client['vendor'],
                        'band': interface['wireless']['frequency'],
                    })




    return render(request, 'ow-makedit/device_status.html', {
        'device': device,
        'device_data': device_data,
        'uptime': uptime,
        'clients': clients
    })

def devices(request):
    from django.contrib import admin
    from django.urls import reverse
    from django.utils.safestring import mark_safe
    # return admin.sites.site._registry[Device].changelist_view(request)
    # options.py:723 (get_changelist_instance)

    cl = admin.sites.site._registry[Device].get_changelist_instance(request)
    cl.formset = None
    def device_status_link(self):
        return mark_safe('<a href="' + reverse('mk-device-status', args=[self.id]) + '"><b>'+self.name+'</b></a>')
    device_status_link.short_description = "name"
    cl.list_display = [device_status_link,'health_status','config_status','mac_address','ip']

    devices = Device.objects.all()
    return render(request, 'ow-makedit/devices.html', {
        'devices': devices,
            'cl': cl,
            'opts': cl.opts,
    })

def map(request):
    return render(request, 'ow-makedit/map.html', {
    })

