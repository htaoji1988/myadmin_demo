from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from common.permission import PermissionVerify
from django.views.generic import TemplateView
from django.contrib import messages


# Create your views here.


def test_adminlte(request):
    return render(request, 'index.html')


def test2(request):
    print(request.user)
    return render(request, 'test.html')


@login_required
def base_page(request):
    messages.add_message(request, messages.INFO, 'Over 9000!', extra_tags='dragonball')
    return render(request, 'mypage/base.html')


@login_required
@PermissionVerify()
def test_permission(request):
    return render(request, 'mypage/test.html')


class generic_v(TemplateView):
    template_name = "mypage/test/"
