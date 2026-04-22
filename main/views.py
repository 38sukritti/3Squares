import os
import logging
from django.shortcuts import render
from django.core.mail import EmailMultiAlternatives
from email.mime.image import MIMEImage
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

def service_detail(request, slug):
    services_data = {
        'corporate-fitouts': {
            'title': 'Corporate Fitouts',
            'tag': 'Corporate',
            'hero_image': 'https://images.unsplash.com/photo-1497366216548-37526070297c?auto=format&fit=crop&w=1600&q=80',
            'description': 'We transform empty shells into high-performing, branded working environments. Our corporate fitout services combine spatial efficiency with elevated aesthetics.',
            'details': [
                'Complete turnkey interior solutions for modern offices.',
                'Acoustic planning and soundproofing for focused work.',
                'Open-plan layout optimization and ergonomic furniture.',
                'Integrated technology and smart office infrastructure.'
            ],
            'process': [
                {'title': 'Analysis', 'desc': 'Understanding your workflow and spatial requirements.'},
                {'title': 'Concept', 'desc': 'Developing a design that reflects your brand identity.'},
                {'title': 'Fit-out', 'desc': 'Precision construction and finishing with premium materials.'}
            ],
            'gallery': [
                'https://images.unsplash.com/photo-1497366754035-f200968a6e72?auto=format&fit=crop&w=800&q=80',
                'https://images.unsplash.com/photo-1497215842964-222b430dc094?auto=format&fit=crop&w=800&q=80',
                'https://images.unsplash.com/photo-1497366811353-6870744d04b2?auto=format&fit=crop&w=800&q=80'
            ]
        },
        'commercial-projects': {
            'title': 'Commercial Projects',
            'tag': 'Projects',
            'hero_image': 'https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?auto=format&fit=crop&w=1600&q=80',
            'description': 'Large-scale commercial developments that demand precision engineering and sophisticated design. From retail hubs to innovation centers.',
            'details': [
                'Scaleable design solutions for large commercial areas.',
                'Integrated MEP and architectural fit-out management.',
                'Material sourcing and logistics for complex projects.',
                'Compliance with international building and safety standards.'
            ],
            'process': [
                {'title': 'Civil Work', 'desc': 'Structural modifications and foundation prep.'},
                {'title': 'Systems', 'desc': 'MEP, HVAC, and Fire Safety integration.'},
                {'title': 'Finishing', 'desc': 'High-spec wall, floor, and ceiling treatments.'}
            ],
            'gallery': [
                '/static/main/images/commercial_project.png',
                '/static/main/images/commercial_project_2.png',
                'https://images.unsplash.com/photo-1497366811353-6870744d04b2?auto=format&fit=crop&w=800&q=80'
            ]
        },
        'coffee-shops': {
            'title': 'Coffee Shops',
            'tag': 'Hospitality',
            'hero_image': 'https://images.unsplash.com/photo-1554118811-1e0d58224f24?auto=format&fit=crop&w=1600&q=80',
            'description': 'Creating the perfect atmosphere for your customers to relax and recharge. We specialize in inviting, Instagrammable café concepts.',
            'details': [
                'Custom coffee counters and ergonomic barista stations.',
                'Atmospheric lighting design for day and night use.',
                'Durable, high-traffic flooring and seating solutions.',
                'Brand-integrated signage and interior theme execution.'
            ],
            'process': [
                {'title': 'Vibe Check', 'desc': 'Setting the mood with lighting and texture.'},
                {'title': 'Workflow', 'desc': 'Optimizing counter speed and seating flow.'},
                {'title': 'Launch', 'desc': 'A finished space ready for opening day.'}
            ],
            'gallery': [
                'https://images.unsplash.com/photo-1442512595331-e89e73853f31?auto=format&fit=crop&w=800&q=80',
                'https://images.unsplash.com/photo-1501339847302-ac426a4a7cbb?auto=format&fit=crop&w=800&q=80',
                'https://images.unsplash.com/photo-1554118811-1e0d58224f24?auto=format&fit=crop&w=800&q=80'
            ]
        },
        'commercial-kitchens': {
            'title': 'Commercial Kitchens',
            'tag': 'Commercial',
            'hero_image': 'https://images.unsplash.com/photo-1556909114-f6e7ad7d3136?auto=format&fit=crop&w=1600&q=80',
            'description': 'Highly functional, sanitary, and ergonomic kitchen environments designed for the rigors of high-volume service.',
            'details': [
                'Industrial-grade stainless steel fabrication.',
                'Optimized workflow layouts for chefs and staff.',
                'Advanced ventilation and grease management systems.',
                'Compliance with strict health and safety regulations.'
            ],
            'process': [
                {'title': 'Layout', 'desc': 'Maximizing efficiency in tight spaces.'},
                {'title': 'Fabrication', 'desc': 'Custom stainless steel work and venting.'},
                {'title': 'Install', 'desc': 'Heavy equipment placement and testing.'}
            ],
            'gallery': [
                '/static/main/images/commercial_kitchen.png',
                'https://images.unsplash.com/photo-1556909114-f6e7ad7d3136?auto=format&fit=crop&w=800&q=80',
                '/static/main/images/commercial_kitchen_3.png'
            ]
        },
        'event-booths': {
            'title': 'Event Booths',
            'tag': 'Exhibition',
            'hero_image': 'https://images.unsplash.com/photo-1540575467063-178a50c2df87?auto=format&fit=crop&w=1600&q=80',
            'description': 'Show-stopping exhibition stands that capture attention from across the floor. Designed for high impact and quick assembly.',
            'details': [
                'Custom modular booth designs for global exhibitions.',
                'Integrated LED displays and high-impact graphics.',
                'Hidden storage and functional meeting areas.',
                'Rapid deployment and precision install services.'
            ],
            'process': [
                {'title': 'Identity', 'desc': 'Translating your brand to a 3D space.'},
                {'title': 'Build', 'desc': 'Pre-fab offsite for flawless onsite setup.'},
                {'title': 'Live', 'desc': 'Handover at the exhibition venue.'}
            ],
            'gallery': [
                '/static/main/images/event_booth_1.png',
                '/static/main/images/event_booth_2.png',
                '/static/main/images/event_booth_3.png'
            ]
        },
        'meeting-areas': {
            'title': 'Meeting & Conf. Areas',
            'tag': 'Corporate',
            'hero_image': 'https://images.unsplash.com/photo-1431540015161-0bf868a2d407?auto=format&fit=crop&w=1600&q=80',
            'description': 'Places for collaboration, decision-making, and high-tech presentations. Boardrooms that impress and huddle rooms that work.',
            'details': [
                'Bespoke boardroom tables with integrated power.',
                'Wall-mounted AV and video conferencing systems.',
                'Acoustic wall panels and sound treatments.',
                'Dimmable, scene-based lighting controls.'
            ],
            'process': [
                {'title': 'Tech Map', 'desc': 'Planning for seamless video and sound.'},
                {'title': 'Acoustics', 'desc': 'Ensuring privacy and clarity.'},
                {'title': 'Furniture', 'desc': 'Custom tables and premium ergonomic seating.'}
            ],
            'gallery': [
                'https://images.unsplash.com/photo-1497366754035-f200968a6e72?auto=format&fit=crop&w=800&q=80',
                'https://images.unsplash.com/photo-1497366216548-37526070297c?auto=format&fit=crop&w=800&q=80',
                'https://images.unsplash.com/photo-1604328698692-f76ea9498e76?auto=format&fit=crop&w=800&q=80'
            ]
        },
        'custom-furniture': {
            'title': 'Custom Furniture',
            'tag': 'Furniture',
            'hero_image': 'https://images.unsplash.com/photo-1538688525198-9b88f6f53126?auto=format&fit=crop&w=1600&q=80',
            'description': 'Unique pieces designed to fit your space perfectly. From reception desks to specialized storage, we craft furniture that lasts.',
            'details': [
                'Bespoke woodworking and CNC precision cuts.',
                'Premium material selection: wood, stone, metal.',
                'Ergonomic design tailored to your specific use.',
                'In-house fabrication for total quality control.'
            ],
            'process': [
                {'title': 'Sketch', 'desc': 'Hand-drawn and CAD concepts.'},
                {'title': 'CRAFT', 'desc': 'Master craftsmanship in our workshop.'},
                {'title': 'Polish', 'desc': 'Final finishing and protective treatments.'}
            ],
            'gallery': [
                '/static/main/images/custom_furniture1.png',
                '/static/main/images/customer_furniture2.png',
                'https://images.unsplash.com/photo-1505691723518-36a5ac3be353?auto=format&fit=crop&w=800&q=80'
            ]
        }
    }
    
    service = services_data.get(slug)
    if not service:
        from django.http import Http404
        raise Http404("Service not found")
        
    return render(request, 'main/service_detail.html', {'service': service})



def _get_email_base(content_html):
    """Wraps email content in the 3Squares branded HTML template."""
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>3Squares Interior Design</title>
</head>
<body style="margin:0;padding:0;background-color:#f4f4f4;font-family:'Segoe UI',Arial,Helvetica,sans-serif;color:#1a1a1a;">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background-color:#f4f4f4;padding:30px 0;">
<tr><td align="center">
<table role="presentation" width="600" cellpadding="0" cellspacing="0" style="max-width:600px;width:100%;background-color:#ffffff;border-radius:16px;overflow:hidden;box-shadow:0 10px 40px rgba(0,0,0,0.08);">

    <!-- Header with brand color -->
    <tr>
        <td style="background-color:#0a2c1c;padding:50px 40px;text-align:center;">
            <!-- Symmetrical Branded Logo (Equal Gaps, Bulletproof) -->
            <img src="cid:logo_cid"
     alt="3Squares Logo"
     width="180"
     style="display:block; margin:0 auto;" />
        </td>
    </tr>

    <!-- Thin accent line -->
    <tr>
        <td style="height:4px;background:linear-gradient(90deg,#0a2c1c,#3cb371,#0a2c1c);"></td>
    </tr>

    <!-- Content area -->
    <tr>
        <td style="padding:40px 40px 30px 40px;">
            {content_html}
        </td>
    </tr>

    <!-- Footer -->
    <tr>
        <td style="background-color:#f9fafb;padding:25px 40px;border-top:1px solid #eee;">
            <table role="presentation" width="100%" cellpadding="0" cellspacing="0">
            <tr>
                <td style="font-size:12px;color:#999;line-height:1.6;">
                    <strong style="color:#0a2c1c;">3Squares Interior Design</strong><br>
                    Ajman, United Arab Emirates<br>
                    <a href="mailto:3squaresid@gmail.com" style="color:#0a2c1c;text-decoration:none;">3squaresid@gmail.com</a> &nbsp;|&nbsp; +971 055 208 2041
                </td>
            </tr>
            <tr>
                <td style="padding-top:15px;font-size:11px;color:#bbb;">
                    &copy; 2026 3Squares Interior Design. All rights reserved.
                </td>
            </tr>
            </table>
        </td>
    </tr>

</table>
</td></tr>
</table>
</body>
</html>"""


def _build_admin_email(name, email, phone, project_type, message):
    """Build the HTML email sent to the 3Squares admin."""
    content = f"""
    <p style="margin:0 0 5px 0;font-size:11px;color:#999;text-transform:uppercase;letter-spacing:2px;font-weight:700;">New Project Inquiry</p>
    <h2 style="margin:0 0 25px 0;font-size:24px;color:#0a2c1c;font-weight:400;font-family:Georgia,'Times New Roman',serif;">A new inquiry has been received</h2>

    <!-- Info Card -->
    <table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background:#f8faf9;border:1px solid #e8ede9;border-radius:12px;margin-bottom:25px;">
        <tr>
            <td style="padding:25px 30px;">
                <table role="presentation" width="100%" cellpadding="0" cellspacing="0">
                    <tr>
                        <td style="padding:8px 0;border-bottom:1px solid #e8ede9;">
                            <span style="font-size:11px;color:#999;text-transform:uppercase;letter-spacing:1.5px;font-weight:700;">Name</span><br>
                            <span style="font-size:16px;color:#1a1a1a;font-weight:600;">{name}</span>
                        </td>
                    </tr>
                    <tr>
                        <td style="padding:12px 0;border-bottom:1px solid #e8ede9;">
                            <span style="font-size:11px;color:#999;text-transform:uppercase;letter-spacing:1.5px;font-weight:700;">Email</span><br>
                            <a href="mailto:{email}" style="font-size:16px;color:#0a2c1c;text-decoration:none;font-weight:600;">{email}</a>
                        </td>
                    </tr>
                    <tr>
                        <td style="padding:12px 0;border-bottom:1px solid #e8ede9;">
                            <span style="font-size:11px;color:#999;text-transform:uppercase;letter-spacing:1.5px;font-weight:700;">Phone</span><br>
                            <span style="font-size:16px;color:#1a1a1a;font-weight:600;">{phone}</span>
                        </td>
                    </tr>
                    <tr>
                        <td style="padding:12px 0;">
                            <span style="font-size:11px;color:#999;text-transform:uppercase;letter-spacing:1.5px;font-weight:700;">Project Type</span><br>
                            <span style="display:inline-block;margin-top:5px;padding:5px 14px;background:#0a2c1c;color:#fff;border-radius:20px;font-size:13px;font-weight:600;letter-spacing:0.5px;">{project_type}</span>
                        </td>
                    </tr>
                </table>
            </td>
        </tr>
    </table>

    <!-- Message -->
    <p style="margin:0 0 8px 0;font-size:11px;color:#999;text-transform:uppercase;letter-spacing:2px;font-weight:700;">Message</p>
    <div style="padding:20px 25px;background:#ffffff;border-left:4px solid #0a2c1c;border-radius:0 8px 8px 0;box-shadow:0 2px 8px rgba(0,0,0,0.04);margin-bottom:25px;">
        <p style="margin:0;font-size:15px;line-height:1.7;color:#4a4a4a;">{message}</p>
    </div>

    <!-- Quick Actions -->
    <table role="presentation" cellpadding="0" cellspacing="0" style="margin:0 auto;">
    <tr>
        <td align="center">
            <a href="mailto:{email}?subject=Re: Your Inquiry - 3Squares Interior Design" style="display:inline-block;padding:14px 35px;background:#0a2c1c;color:#ffffff;text-decoration:none;border-radius:30px;font-size:14px;font-weight:700;letter-spacing:1px;">Reply to {name}</a>
        </td>
    </tr>
    </table>
    """
    return _get_email_base(content)


def _build_user_email(name, project_type):
    """Build the HTML confirmation email sent to the user."""
    content = f"""
    <p style="margin:0 0 5px 0;font-size:11px;color:#999;text-transform:uppercase;letter-spacing:2px;font-weight:700;">Inquiry Confirmed</p>
    <h2 style="margin:0 0 8px 0;font-size:28px;color:#0a2c1c;font-weight:400;font-family:Georgia,'Times New Roman',serif;">Thank you, {name}!</h2>
    <p style="margin:0 0 30px 0;font-size:15px;color:#4a4a4a;line-height:1.7;">We're thrilled that you're considering 3Squares for your project. Your inquiry has been received and our design team is already reviewing the details.</p>

    <!-- Project Type Badge -->
    <table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background:linear-gradient(135deg,#f8faf9 0%,#eef3f0 100%);border:1px solid #e0e8e3;border-radius:12px;margin-bottom:30px;">
        <tr>
            <td style="padding:25px 30px;text-align:center;">
                <span style="font-size:11px;color:#999;text-transform:uppercase;letter-spacing:2px;font-weight:700;">Your Project</span><br>
                <span style="display:inline-block;margin-top:10px;padding:8px 20px;background:#0a2c1c;color:#fff;border-radius:25px;font-size:15px;font-weight:700;letter-spacing:1px;">{project_type}</span>
            </td>
        </tr>
    </table>

    <!-- What happens next -->
    <p style="margin:0 0 15px 0;font-size:11px;color:#999;text-transform:uppercase;letter-spacing:2px;font-weight:700;">What happens next?</p>

    <table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="margin-bottom:30px;">
        <tr>
            <td style="padding:12px 0;border-bottom:1px solid #f0f0f0;">
                <table role="presentation" cellpadding="0" cellspacing="0">
                <tr>
                    <td style="vertical-align:top;padding-right:15px;">
                        <div style="width:30px;height:30px;background:#0a2c1c;color:#fff;border-radius:50%;text-align:center;line-height:30px;font-size:13px;font-weight:700;">1</div>
                    </td>
                    <td style="vertical-align:top;">
                        <strong style="font-size:14px;color:#1a1a1a;">Review</strong><br>
                        <span style="font-size:13px;color:#666;line-height:1.5;">Our design team will review your project requirements within 24 hours.</span>
                    </td>
                </tr>
                </table>
            </td>
        </tr>
        <tr>
            <td style="padding:12px 0;border-bottom:1px solid #f0f0f0;">
                <table role="presentation" cellpadding="0" cellspacing="0">
                <tr>
                    <td style="vertical-align:top;padding-right:15px;">
                        <div style="width:30px;height:30px;background:#0a2c1c;color:#fff;border-radius:50%;text-align:center;line-height:30px;font-size:13px;font-weight:700;">2</div>
                    </td>
                    <td style="vertical-align:top;">
                        <strong style="font-size:14px;color:#1a1a1a;">Consultation</strong><br>
                        <span style="font-size:13px;color:#666;line-height:1.5;">We'll reach out to schedule a free consultation to discuss your vision.</span>
                    </td>
                </tr>
                </table>
            </td>
        </tr>
        <tr>
            <td style="padding:12px 0;">
                <table role="presentation" cellpadding="0" cellspacing="0">
                <tr>
                    <td style="vertical-align:top;padding-right:15px;">
                        <div style="width:30px;height:30px;background:#0a2c1c;color:#fff;border-radius:50%;text-align:center;line-height:30px;font-size:13px;font-weight:700;">3</div>
                    </td>
                    <td style="vertical-align:top;">
                        <strong style="font-size:14px;color:#1a1a1a;">Proposal</strong><br>
                        <span style="font-size:13px;color:#666;line-height:1.5;">You'll receive a tailored proposal with design concepts and a project timeline.</span>
                    </td>
                </tr>
                </table>
            </td>
        </tr>
    </table>

    <!-- CTA -->
    <table role="presentation" cellpadding="0" cellspacing="0" style="margin:0 auto;">
    <tr>
        <td align="center">
            <a href="https://threesquares.onrender.com/portfolio/" style="display:inline-block;padding:14px 35px;background:#0a2c1c;color:#ffffff;text-decoration:none;border-radius:30px;font-size:14px;font-weight:700;letter-spacing:1px;">View Our Portfolio</a>
        </td>
    </tr>
    </table>

    <p style="margin:25px 0 0 0;font-size:14px;color:#4a4a4a;line-height:1.7;text-align:center;">
        Have questions? Reach out at <a href="mailto:3squaresid@gmail.com" style="color:#0a2c1c;font-weight:600;text-decoration:none;">3squaresid@gmail.com</a><br>
        or call us at <strong style="color:#0a2c1c;">+971 055 208 2041</strong>
    </p>
    """
    return _get_email_base(content)


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

        # Check if email is configured before attempting to send
        if not settings.EMAIL_HOST_PASSWORD:
            logger.error("EMAIL_HOST_PASSWORD is not set. Skipping email send.")
            messages.success(request, "Your inquiry has been received! We'll get back to you soon.")
        else:
            try:
                # Path to logo for CID embedding (source of truth)
                logo_path = os.path.join(settings.BASE_DIR, 'main', 'static', 'main', 'images', 'logo_white.png')
                logo_data = None
                if os.path.exists(logo_path):
                    try:
                        with open(logo_path, 'rb') as f:
                            logo_data = f.read()
                    except Exception as e:
                        logger.error(f"Error reading logo file: {e}")

                # 1. HTML email to Admin
                admin_html = _build_admin_email(name, email, phone, project_type, message)
                admin_email = EmailMultiAlternatives(
                    subject=f"New Inquiry from {name} - 3Squares Interior Design",
                    body=f"New Inquiry from {name}. Please view in an HTML compatible email client.",
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    to=['3squaresid@gmail.com'],
                )
                admin_email.attach_alternative(admin_html, "text/html")
                
                if logo_data:
                    try:
                        logo = MIMEImage(logo_data)
                        logo.add_header('Content-ID', '<logo_cid>')
                        admin_email.attach(logo)
                        # Set subtype to 'related' only if there's an inline attachment
                        admin_email.mixed_subtype = 'related'
                    except Exception as e:
                        logger.error(f"Error attaching logo to admin email: {e}")

                admin_email.send(fail_silently=False)
                logger.info(f"Admin notification email sent for inquiry from {name}")

                # 2. HTML confirmation email to User
                user_html = _build_user_email(name, project_type)
                user_email = EmailMultiAlternatives(
                    subject="We've received your inquiry - 3Squares Interior Design",
                    body=f"Thank you {name}, we've received your inquiry. Please view in an HTML compatible email client.",
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    to=[email],
                )
                user_email.attach_alternative(user_html, "text/html")
                
                if logo_data:
                    try:
                        logo = MIMEImage(logo_data)
                        logo.add_header('Content-ID', '<logo_cid>')
                        user_email.attach(logo)
                        user_email.mixed_subtype = 'related'
                    except Exception as e:
                        logger.error(f"Error attaching logo to user email: {e}")

                user_email.send(fail_silently=False)
                logger.info(f"Confirmation email sent to {email}")

                messages.success(request, "Your message has been sent successfully! We'll get back to you soon.")
            except Exception as e:
                logger.error(f"Email sending failed: {type(e).__name__}: {e}")
                # Provide more context if it's an authentication error
                error_msg = str(e)
                if "530" in error_msg:
                    messages.warning(request, "Authentication failed. Please check your SMTP credentials.")
                else:
                    messages.warning(request, "Your inquiry has been received, but we couldn't send a confirmation email. Our team will still contact you shortly.")

    return render(request, 'main/contact.html')
