from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required(login_url='/users/login')
def home(request):
    last_name = request.session['last_name']
    return render_to_response('base/home.html',{'last_name':last_name})


@login_required(login_url='/users/login')
def host_list(request):
    return render_to_response('base/host_list.html')