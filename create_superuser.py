from django.contrib.auth.models import User

if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser(
        username='3Squares',
        email='[3squaresid@gmail.com]',
        password='3Squares@123'
    )