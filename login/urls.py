from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.rewrite, name='rewrite'),
    path('login/', views.logins, name='login'),
    path('logout/', views.logout, name="logout"),
    path('permission/deny/', views.NoPermission, name='permissiondenyurl'),
    path('user_manage/', views.user_manage, name='user_manage'),
    path('user_add/', views.user_add, name='user_add'),
    path('user_del/', views.user_del, name='user_del'),
    path('user_update/', views.user_update, name='user_update'),
    path('user_permission/', views.permission_manage, name='user_permission')
]
