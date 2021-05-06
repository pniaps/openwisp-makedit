import uuid
from datetime import datetime
from dateutil.relativedelta import relativedelta
from django.shortcuts import render
from swapper import load_model

Device = load_model('config', 'Device')
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




    return render(request, 'device_status.html', {
        'device': device,
        'device_data': device_data,
        'uptime': uptime,
        'clients': clients
    })
