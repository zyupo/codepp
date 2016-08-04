from django.shortcuts import render,render_to_response
from django.contrib.auth.decorators import login_required
from .models import Monitor_server
# Create your views here.

@login_required(login_url='/login')
def service(request):
    return render_to_response('monitor/service.html')



#add server monitor
def addServermonitor(request):
    if request.method == 'POST':
        server_name = request('server_name')
        server_ip = request.server_ip
        # server_ip = request.GET.get('server_ip', '')
        # server_port = request.GET.get('server_port', '')
        print(server_name)
        # print(server_ip)
        # print(server_port)
        return server_name