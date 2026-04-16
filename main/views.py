import logging
from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings
from .models import Inquiry

logger = logging.getLogger(__name__)

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

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        project_type = request.POST.get('project-type', '')
        message = request.POST.get('message', '')

        # Save to Database first (independent of email)
        try:
            Inquiry.objects.create(
                name=name,
                email=email,
                phone=phone,
                project_type=project_type,
                message=message
            )
            logger.info(f"Inquiry saved to database from {name} ({email})")
        except Exception as e:
            logger.error(f"Failed to save inquiry to database: {e}")

        # 1. Inquiry mail to 3Squares (Site Owner)
        admin_subject = f"New Inquiry from {name} - 3Squares Interior Design"
        admin_message = f"""
        New project inquiry received:
        
        Name: {name}
        Email: {email}
        Phone: {phone}
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

        # Check if email is configured before attempting to send
        if not settings.EMAIL_HOST_PASSWORD:
            logger.error("EMAIL_HOST_PASSWORD is not set. Skipping email send.")
            messages.success(request, "Your inquiry has been received! We'll get back to you soon.")
        else:
            try:
                # Send to Admin
                send_mail(
                    admin_subject,
                    admin_message,
                    settings.DEFAULT_FROM_EMAIL,
                    ['3squaresid@gmail.com'],
                    fail_silently=False,
                )
                logger.info(f"Admin notification email sent for inquiry from {name}")
                
                # Send Confirmation to User
                send_mail(
                    user_subject,
                    user_message,
                    settings.DEFAULT_FROM_EMAIL,
                    [email],
                    fail_silently=False,
                )
                logger.info(f"Confirmation email sent to {email}")
                
                messages.success(request, "Your message has been sent successfully! We'll get back to you soon.")
            except Exception as e:
                logger.error(f"Email sending failed: {type(e).__name__}: {e}")
                messages.warning(request, "Your inquiry has been received, but we couldn't send a confirmation email. Our team will still contact you shortly.")

    return render(request, 'main/contact.html')
