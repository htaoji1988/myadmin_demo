from django.shortcuts import render, HttpResponse


# Create your views here.


def test_adminlte(request):
    return render(request, 'index.html')


def test2(request):
    print(request.user)
    return render(request, 'test.html')


def base_page(request):
    return render(request, 'base.html')
