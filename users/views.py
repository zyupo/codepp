from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import auth,sessions
from django.contrib.auth.models import User ,UserManager

#登录
def user_login(request):
    if request.method != 'POST':
        return render_to_response('users/login.html')
    else:
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        error = []
        if not username or not  password:
            error.append('账号或者密码不能为空')
            return render_to_response('users/login.html',{'error':error})
        user = auth.authenticate(username=username,password=password)
        if user is not None and user.is_active:
            auth.login(request,user)
            lastname = request.session['last_name']
            return HttpResponseRedirect('base/home',lastname)
        else:
            error.append('账号或者密码错误')
            return render_to_response('users/login.html',{'error':error})



#@login_required(login_url='/book/login/')
def user_logout(request):
    auth.logout(request)
    return HttpResponseRedirect("login")




def user_list(request):
    user_info = User.objects.all()
    return render_to_response('users/user_list.html',{'user_info':user_info})



def add_user(request):
    UserManager.create_user()