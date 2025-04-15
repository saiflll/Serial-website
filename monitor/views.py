from django.shortcuts import render, redirect
from django.http import JsonResponse
from . import serial_reader

def index(request):
    ports = serial_reader.list_ports()
    connected = serial_reader.port
    return render(request, 'monitor/index.html', {
        'ports': ports,
        'connected': connected
    })

def select_port(request):
    if request.method == 'POST':
        port = request.POST.get('port')
        success = serial_reader.connect(port)
        return redirect('/')
    return redirect('/')

def serial_data(request):
    return JsonResponse({'data': serial_reader.get_data()})