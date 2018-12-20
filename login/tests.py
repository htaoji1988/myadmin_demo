from django.test import TestCase
from .models import User, UserManager

# Create your tests here.

user = User.objects.create_user(email="zhanhui.chen@99bill.com", username='zhanhui.chen', password="12345678")
user.save()

# user = User.objects.get(username="jie.liu")
# user.role_id = 1
# user.save()
