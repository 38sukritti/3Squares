import os
import django

# 👇 VERY IMPORTANT (replace with your project name)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dubai_project.settings')

django.setup()

from django.contrib.auth.models import User

if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser(
        username='3Squares',
        email='[3squaresid@gmail.com]',
        password='3Squares@123'
    )