from django.test import TestCase
from .models import User, UserManager

# Create your tests here.

user = User.objects.create_user(email="haitao.ji@99bill.com", username='haitao.ji', password="q5920868")
user.save()

# user = User.objects.get(username="jie.liu")
# user.role_id = 1
# user.save()
