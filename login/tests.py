from django.test import TestCase
from django.contrib.auth.models import User
# Create your tests here.

user = User.objects.get(username='htaoji1988')
user.set_password("q5920868")
user.save()
