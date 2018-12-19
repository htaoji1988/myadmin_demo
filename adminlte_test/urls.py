from django.contrib import admin
from django.urls import path
from adminlte_test import views as adminlte_test_vies

urlpatterns = [
    path('basic/', adminlte_test_vies.base_page),
    path('all/', adminlte_test_vies.test2),
    path('permission_test/', adminlte_test_vies.test_permission),
]
