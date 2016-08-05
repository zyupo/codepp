from django.shortcuts import render,render_to_response,HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Server_info
# from django.http import JsonResponse
# Create your views here.

@login_required(login_url='/login')
def service(request):
    server_status = Server_info.objects.all()
    return render_to_response('monitor/service.html',{'server_status':server_status})



#add server monitor
def addServermonitor(request):
    if request.method == 'POST':
        server_name = request.POST.get("server_name",'')
        server_ip = request.POST.get("server_ip", '')
        server_port = request.POST.get("server_port", '')
        s_info = Server_info.objects.create(server_name=server_name,server_ip=server_ip,server_port=server_port,server_status=1)

        if s_info:
            return HttpResponse('success')
        else:
            return HttpResponse('failed')
    else:
        return False