from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import auth,sessions
from django.contrib.auth.models import User ,UserManager
from django.contrib.auth.decorators import login_required
from codepp.common import *

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



def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/base/home')



@require_role()
def user_list(request):
    user_info = User.objects.all()
    return render_to_response('users/user_list.html',{'user_info':user_info})


@require_role()
def user_edit(request):
    if request.method == 'GET':
        user_id = request.GET.get('id','')
        if not user_id:
            return HttpResponseRedirect('/base/home')

        user = User.objects.get(id=user_id)
        return render_to_response('users/user_edit.html',{'user':user})
    else:
        user_id = request.GET.get('id','')
        username = request.GET.get('username','')
        last_name = request.GET.get('last_name')
        password = request.GET.get('password','')
        email = request.GET.get('email','')
        active = request.GET.get('active','')
        is_active = True if '1' in active else False


        # print(username);exit()
        if user_id:
            user = User.objects.get(id=user_id)
            user_query = User.objects.filter(id=user_id)
            user_query.update(username=username,last_name=last_name,email=email,is_active=is_active)
            if password != '':
                password = user.set_password(password)
            user.save()
            return HttpResponseRedirect('/users/user_list')
        else:
            return HttpResponseRedirect('user_list')










@require_role()
def add_user(request):
    UserManager.create_user()