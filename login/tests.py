from django.test import TestCase
from .models import User, UserManager
import os

# Create your tests here.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(os.path.join(BASE_DIR, 'AdminLTE'),)