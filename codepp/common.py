from django.http import HttpResponseRedirect


# def require_role(role='user'):
#     """
#     decorator for require user role in ["super", "admin", "user"]
#     要求用户是某种角色 ["super", "admin", "user"]的装饰器
#     """
#
#     def _deco(func):
#         def __deco(request, *args, **kwargs):
#             # request.session['pre_url'] = request.path
#             if not request.user.is_authenticated():
#                 return HttpResponseRedirect('login')
#             if role == 'admin':
#                 if request.user.role == 'CU':
#                     return HttpResponseRedirect('index')
#             elif role == 'super':
#                 if request.user.role in ['CU', 'GA']:
#                     return HttpResponseRedirect('index')
#             return func(request, *args, **kwargs)
#         return __deco
#     return _deco
#
#



def require_role(role='user'):
    """
    decorator for require user role in ["super", "admin", "user"]
    要求用户是某种角色 ["super", "admin", "user"]的装饰器
    """
    def _deco(func):
        def __deco(request, *args, **kwargs):
            # request.session['pre_url'] = request.path
            if not request.user.is_authenticated():
                return HttpResponseRedirect('/login')
            return func(request, *args, **kwargs)
        return __deco
    return _deco
