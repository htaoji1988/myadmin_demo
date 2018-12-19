from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required


# Create your views here.


def test_adminlte(request):
    return render(request, 'index.html')


def test2(request):
    print(request.user)
    return render(request, 'test.html')


@login_required
def base_page(request):
    return render(request, 'mypage/base.html')

@login_required
def test_permission(request):
    return render(request,'mypage/test.html')
