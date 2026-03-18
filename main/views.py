from django.shortcuts import render, redirect
from django.utils.translation import gettext as _
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings

from .models import ContactInquiry, JobApplication


# ===============================
# HOME
# ===============================
def home_view(request):
    return render(request, 'main/home.html', {
        "title": _("Home")
    })


# ===============================
# ABOUT
# ===============================
def about_view(request):
    return render(request, 'main/about.html', {
        "title": _("About Us")
    })


# ===============================
# SERVICES
# ===============================
def services_view(request):
    return render(request, 'main/services.html', {
        "title": _("Our Services")
    })


# ===============================
# CAREERS
# ===============================
def careers_view(request):
    if request.method == "POST":
        full_name = request.POST.get('name')
        email = request.POST.get('email')
        position = request.POST.get('position')
        cover_letter = request.POST.get('cover_letter')
        resume = request.FILES.get('resume')

        try:
            JobApplication.objects.create(
                full_name=full_name,
                email=email,
                position=position,
                cover_letter=cover_letter,
                resume=resume
            )
            messages.success(
                request,
                _("Application submitted successfully. Our HR team will contact you.")
            )
        except Exception as e:
            print(f"Career application error: {e}")
            messages.error(
                request,
                _("There was an error submitting your application. Please try again.")
            )

        return redirect('careers')

    return render(request, 'main/careers.html', {
        "title": _("Careers")
    })


# ===============================
# CONTACT
# ===============================
def contact_view(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject_category = request.POST.get('subject')
        message = request.POST.get('message')

        try:
            # Save inquiry
            ContactInquiry.objects.create(
                name=name,
                email=email,
                subject=subject_category,
                message=message
            )

            context = {
                "name": name,
                "email": email,
                "subject": subject_category,
                "message": message
            }

            # -------- Admin Email --------
            admin_html = render_to_string('emails/contact_admin.html', context)
            admin_text = strip_tags(admin_html)

            admin_email = EmailMultiAlternatives(
                subject=f"New Contact Inquiry: {subject_category}",
                body=admin_text,
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=[settings.CONTACT_EMAIL]
            )
            admin_email.attach_alternative(admin_html, "text/html")
            admin_email.send()

            # -------- User Confirmation --------
            user_html = render_to_string('emails/contact_confirmation.html', context)
            user_text = strip_tags(user_html)

            user_email = EmailMultiAlternatives(
                subject=_("Thank you for contacting SolutionsTestLab"),
                body=user_text,
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=[email]
            )
            user_email.attach_alternative(user_html, "text/html")
            user_email.send()

            messages.success(
                request,
                _("Your message has been sent successfully. We will get back to you shortly.")
            )

        except Exception as e:
            print(f"Contact form error: {e}")
            messages.error(
                request,
                _("An error occurred while sending your message. Please try again later.")
            )

        return redirect('contact')

    return render(request, 'main/contact.html', {
        "title": _("Contact Us")
    })
