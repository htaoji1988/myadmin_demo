from django.shortcuts import render, HttpResponseRedirect, HttpResponse


# Create your views here.

def rewrite(request):
    return HttpResponseRedirect("/login/")


def login(request):
    if request.method == "POST":
        user = request.POST.get("user")
        print(str(user))
        password = request.POST.get("password")
        print(str(password))
        return HttpResponse("666")
    else:
        return render(request, 'mypage/login/login.html')
