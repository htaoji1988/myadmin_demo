from django.shortcuts import render, HttpResponseRedirect
from django.http import JsonResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.db.models import Q
from common.permission import PermissionVerify
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
            user_role = User.objects.get(username=username).role
            request.session['username'] = username
            request.session['password'] = password
            request.session['rolename'] = str(user_role)
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


@login_required
def user_manage(request):
    user_objs = User.objects.filter()
    res_list = []
    for i in user_objs:
        dic = {}
        dic['username'] = i.username
        dic['nickname'] = i.nickname
        dic['sex'] = i.sex
        dic['email'] = i.email
        dic['status'] = i.is_active
        dic['role'] = i.role
        dic['last_login'] = i.last_login
        res_list.append(dic)
    role_objs = RoleList.objects.filter()
    role_list = []
    for i in role_objs:
        role_list.append(i.name)
    return render(request, 'mypage/login/user_manage.html', {"result_list": res_list, "role_list": role_list})


@login_required
def role_manage(request):
    role_objs = RoleList.objects.filter()
    res_list = []
    for i in role_objs:
        dic = {}
        dic['id'] = i.id
        dic['name'] = i.name
        res_list.append(dic)
    return render(request, 'mypage/login/user_role.html', {"result_list": res_list})


@login_required
def permission_manage(request):
    role_objs = PermissionList.objects.filter()
    res_list = []
    for i in role_objs:
        dic = {}
        dic['id'] = i.id
        dic['name'] = i.name
        dic['url'] = i.url
        res_list.append(dic)
    return render(request, 'mypage/login/user_permission.html', {"result_list": res_list})


@login_required
def permission_add(request):
    if request.method == "POST":
        name = request.POST.get("permission_name")
        url = request.POST.get("permission_url")
        kwargs = {}
        obj_exsit = PermissionList.objects.filter(Q(name=name) | Q(url=url))
        if obj_exsit:
            res_dic = {
                "result": "false",
                "content": "name 或者 url已经存在，无法重复添加"
            }
        else:
            kwargs['name'] = name
            kwargs['url'] = url
            try:
                PermissionList.objects.create(**kwargs)
                print(kwargs)
                res_dic = {
                    "result": "success",
                    "content": ""
                }
            except Exception as e:
                res_dic = {
                    "result": "success",
                    "content": e
                }
        return JsonResponse(res_dic)


@login_required
def permission_update(request):
    if request.method == "POST":
        id = request.POST.get("permission_id")
        print()
        kwargs = {
            "name": request.POST.get("permission_name"),
            "url": request.POST.get("permission_url")
        }
        res_dic = {}
        obj_permission = PermissionList.objects.filter(id=id)
        if obj_permission:
            try:
                obj_permission.update(**kwargs)
                res_dic = {
                    "result": "success",
                    "content": ""
                }
            except Exception as e:
                res_dic = {
                    "result": "false",
                    "content": e
                }

        return JsonResponse(res_dic)


@login_required
def permission_del(request):
    if request.method == "POST":
        res_dic = {}
        id = request.POST.get("permission_id")
        obj_permission = PermissionList.objects.get(id=id)
        if obj_permission:
            try:
                obj_permission.delete()
                res_dic = {
                    "result": "success",
                    "content": ""
                }
            except Exception as e:
                res_dic = {
                    "result": "false",
                    "content": e
                }
        return JsonResponse(res_dic)


@login_required
def user_add(request):
    if request.method == "POST":
        user = request.POST.get("user_name")
        if (User.objects.filter(username=user)):
            return JsonResponse({"result": "false", "content": "用户已经存在"})

        dic = {
            "username": request.POST.get("user_name"),
            "password": request.POST.get("passwd"),
            "email": request.POST.get("email"),
        }
        user = User.objects.create_user(**dic)
        user.save()

        if (request.POST.get("isactive") == "启用"):
            status = True
        else:
            status = False

        role = request.POST.get("role")
        role_obj = RoleList.objects.filter(name=role)
        if role_obj:
            role_id = role_obj[0].id
        else:
            role_id = None
        dic2 = {
            "sex": request.POST.get("sex"),
            "is_active": status,
            "nickname": request.POST.get("nickname"),
            "role_id": role_id
        }

        User.objects.filter(username=user).update(**dic2)
        return JsonResponse({"result": "success"})


@login_required
def user_del(request):
    if request.method == "POST":
        user = request.POST.get("user_name")
        obj_user = User.objects.filter(username=user)
        if obj_user:
            obj_user.delete()
            return JsonResponse({"result": "success"})
        else:
            return JsonResponse({"result": "false", "content": "出现了一些异常"})


@login_required
def user_update(request):
    if request.method == "POST":
        username = request.POST.get("user_name")
        if request.POST.get("isactive") == "启用":
            isactive = True
        else:
            isactive = False

        role = request.POST.get("role")
        role_obj = RoleList.objects.filter(name=role)
        if role_obj:
            role_id = role_obj[0].id
        else:
            role_id = None

        kwargs = {
            "nickname": request.POST.get("nickname"),
            "sex": request.POST.get("sex"),
            "email": request.POST.get("email"),
            "is_active": isactive,
            "role_id": role_id
        }
        user_obj = User.objects.filter(username=username)
        try:
            user_obj.update(**kwargs)
            return JsonResponse({"result": "success"})
        except Exception as e:
            return JsonResponse({"result": "false", "content": e})
