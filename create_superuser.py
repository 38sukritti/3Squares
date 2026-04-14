import os
import django

# Set the settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dubai_project.settings')
django.setup()

from django.contrib.auth.models import User

username = '3Squares'
email = '3squaresid@gmail.com'
password = '3Squares@123'

if not User.objects.filter(username=username).exists():
    print(f"Creating superuser {username}...")
    User.objects.create_superuser(
        username=username,
        email=email,
        password=password
    )
    print("Superuser created successfully.")
else:
    print(f"Superuser {username} already exists.")