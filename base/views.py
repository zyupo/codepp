from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required(login_url='/users/user_login/')
def home(request,name):
    name = request.name
    return render_to_response('base/home.html',{'name':name})


@login_required(login_url='/users/user_login/')
def host_list(request):
    return render_to_response('base/host_list.html')