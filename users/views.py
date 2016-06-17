from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import auth,sessions
from django.contrib.auth.models import User ,UserManager
from django.contrib.auth.decorators import login_required
from ..codepp.common import *


#登录
def login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/base/home')
    if request.method != 'POST':
        return render_to_response('login.html')
    else:
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        error = []
        if not username or not  password:
            error.append('账号或者密码不能为空')
            return render_to_response('login.html',{'error':error})
        user = auth.authenticate(username=username,password=password)
        if user is not None and user.is_active:
            auth.login(request,user)
            request.session['last_name'] = user.last_name
            return HttpResponseRedirect('/base/home')
        else:
            error.append('账号或者密码错误')
            return render_to_response('login.html',{'error':error})



#@login_required(login_url='/book/login/')
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/base/home')



@require_role()
def user_list(request):
    user_info = User.objects.all()
    return render_to_response('users/user_list.html',{'user_info':user_info})



def add_user(request):
    UserManager.create_user()