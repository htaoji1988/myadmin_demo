from django.contrib import admin
from django.urls import path
from adminlte_test import views as adminlte_test_vies

urlpatterns = [
    path('adminlte_test/', adminlte_test_vies.test_adminlte),
    path('test2/', adminlte_test_vies.test2)
]
