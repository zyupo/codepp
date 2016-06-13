from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import auth



#登录
def login(request):
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
            return HttpResponseRedirect('base/home')
        else:
            error.append('账号或者密码错误')
            return render_to_response('users/login.html',{'error':error})



# @login_required(login_url='/book/login/')
# def logout(request):
#     auth.logout(request)
#     return HttpResponseRedirect("/book/login/")
#     # return render_to_response('login.html')