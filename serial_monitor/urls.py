from django.contrib import admin
from django.urls import path
from monitor.views import index, serial_data, select_port

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('serial/', serial_data),
    path('select_port/', select_port, name='select_port'),
]