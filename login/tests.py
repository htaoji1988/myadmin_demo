from django.test import TestCase
from django.contrib.auth.models import User
# Create your tests here.

user = User.objects.create_user(username='haitao.ji',password="q5920868")
user.save()
