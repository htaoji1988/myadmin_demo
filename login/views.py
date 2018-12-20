from django.shortcuts import render, HttpResponseRedirect
from django.http import JsonResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from .models import User, RoleList, PermissionList


# Create your views here.

def rewrite(request):
    return HttpResponseRedirect("/login/")


def logins(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            request.session['username'] = username
            request.session['password'] = password
            return HttpResponseRedirect(request.GET.get('next', '/test/basic/'))
        else:
            message = """用户名或者密码不正确"""
            return render(request, 'mypage/login/login.html', {'message': message, })
    else:
        return render(request, 'mypage/login/login.html')


def logout(request):
    if request.method == "POST":
        auth.logout(request)
        return JsonResponse({"status": "ok"})


@login_required
def NoPermission(request):
    return render(request, 'mypage/login/permission.no.html')
