from django.contrib import admin
from django.urls import path
from adminlte_test import views as adminlte_test_views

urlpatterns = [
    path('basic/', adminlte_test_views.base_page, name='basic'),
    path('all/', adminlte_test_views.test2),
    path('permission_test/', adminlte_test_views.test_permission),
]
