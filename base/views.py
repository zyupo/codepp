from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import auth

# Create your views here.



def home(request):
    return render_to_response('base/home.html')



def host_list(request):
    return render_to_response('base/host_list.html')