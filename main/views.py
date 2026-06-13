from django.contrib import messages
from django.shortcuts import render, redirect
from django.utils.translation import gettext as _
from django.core.mail import EmailMessage, send_mail
from django.conf import settings


def home(request):
    return render(request, "main/home.html")


def about(request):
    return render(request, "main/about.html")


def services(request):
    return render(request, "main/services.html")


def quality_assurance(request):
    return render(request, "main/quality_assurance.html")


def software_testing(request):
    return render(request, "main/software_testing.html")


def test_management(request):
    return render(request, "main/test_management.html")


def careers(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        position = request.POST.get("position")
        cover_letter = request.POST.get("cover_letter")
        resume = request.FILES.get("resume")

        company_subject = f"New Job Application - {position}"

        company_message = f"""
New application received.

Name: {name}
Email: {email}
Position: {position}

Cover Letter:
{cover_letter}
"""

        company_email = EmailMessage(
            subject=company_subject,
            body=company_message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=["careers@solutionstestlab.com"],
            reply_to=[email],
        )

        if resume:
            company_email.attach(
                resume.name,
                resume.read(),
                resume.content_type
            )

        company_email.send(fail_silently=False)

        applicant_subject = "Application Received | SolutionsTestLab"

        applicant_message = f"""
Dear {name},

Thank you for applying to SolutionsTestLab.

We have successfully received your application for the position of:

{position}

Our recruitment team will carefully review your profile and contact you if your qualifications match our current needs.

We appreciate your interest in joining SolutionsTestLab.

Best regards,
SolutionsTestLab Recruitment Team

Eagle-Eye Precision in every line of code.
"""

        send_mail(
            applicant_subject,
            applicant_message,
            settings.DEFAULT_FROM_EMAIL,
            [email],
            fail_silently=False,
        )

        messages.success(
            request,
            _("Your application has been submitted successfully.")
        )

        return redirect("careers")

    return render(request, "main/careers.html")


def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")
        consent = request.POST.get("consent")

        company_subject = f"New Contact Message - {subject}"

        company_message = f"""
New contact message received.

Name: {name}
Email: {email}
Subject: {subject}
Consent: {consent}

Message:
{message}
"""

        send_mail(
            company_subject,
            company_message,
            settings.DEFAULT_FROM_EMAIL,
            ["info@solutionstestlab.com"],
            fail_silently=False,
        )

        applicant_subject = "Message Received | SolutionsTestLab"

        applicant_message = f"""
Dear {name},

Thank you for contacting SolutionsTestLab.

We have successfully received your message regarding:

{subject}

Our team will review your inquiry and get back to you shortly.

Best regards,
SolutionsTestLab Team

Eagle-Eye Precision in every line of code.
"""

        send_mail(
            applicant_subject,
            applicant_message,
            settings.DEFAULT_FROM_EMAIL,
            [email],
            fail_silently=False,
        )

        messages.success(
            request,
            _("Your message was sent successfully.")
        )

        return redirect("contact")

    return render(request, "main/contact.html")

def impressum(request):
    return render(request, "main/impressum.html")

def privacy_policy(request):
    return render(request, "main/privacy_policy.html")
