from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.rewrite, name='rewrite'),
    path('login/', views.logins, name='login'),
    path('logout/', views.logout, name="logout"),
    path('permission/deny/', views.NoPermission, name='permissiondenyurl'),
]
