from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings

def index(request):
    return render(request, 'main/index.html')

def home(request):
    return render(request, 'main/home.html')

def about(request):
    return render(request, 'main/about.html')

def services(request):
    return render(request, 'main/services.html')

def portfolio(request):
    return render(request, 'main/portfolio.html')

def membership(request):
    return render(request, 'main/membership.html')

from .models import Inquiry

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        project_type = request.POST.get('project-type')
        message = request.POST.get('message')

        # Save to Database
        Inquiry.objects.create(
            name=name,
            email=email,
            phone=phone,
            project_type=project_type,
            message=message
        )

        # 1. Inquiry mail to 3Squares (Site Owner)
        admin_subject = f"New Inquiry from {name} - 3Squares Interior Design"
        admin_message = f"""
        New project inquiry received:
        
        Name: {name}
        Email: {email}
        Project Type: {project_type}
        
        Message:
        {message}
        """
        
        # 2. Confirmation mail to User
        user_subject = "We've received your inquiry - 3Squares Interior Design"
        user_message = f"""
        Dear {name},
        
        Thank you for reaching out to 3Squares Interior Design. 
        
        We have received your inquiry regarding your "{project_type}" project and our team will review it shortly. Somebody will contact you soon to discuss the details.
        
        Best regards,
        The 3Squares Team
        """

        try:
            # Send to Admin
            send_mail(
                admin_subject,
                admin_message,
                settings.DEFAULT_FROM_EMAIL,
                ['3squaresid@gmail.com'],
                fail_silently=False,
            )
            
            # Send Confirmation to User
            send_mail(
                user_subject,
                user_message,
                settings.DEFAULT_FROM_EMAIL,
                [email],
                fail_silently=False,
            )
            
            messages.success(request, "Your message has been sent successfully! We'll get back to you soon.")
        except Exception as e:
            messages.error(request, f"There was an error sending your message. Please try again later. ({str(e)})")

    return render(request, 'main/contact.html')
