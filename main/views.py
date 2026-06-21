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

        try:
            company_email = EmailMessage(
                subject=f"New Job Application - {position}",
                body=f"""
New application received.

Name: {name}
Email: {email}
Position: {position}

Cover Letter:
{cover_letter}
""",
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=["info@solutionstestlab.com"],
                reply_to=[email],
            )

            if resume:
                company_email.attach(
                    resume.name,
                    resume.read(),
                    resume.content_type
                )

            company_email.send(fail_silently=False)

            send_mail(
                "Application Received | SolutionsTestLab",
                f"""
Dear {name},

Thank you for applying to SolutionsTestLab.

We have successfully received your application for the position of:

{position}

Our recruitment team will carefully review your profile and contact you if your qualifications match our current needs.

Best regards,
SolutionsTestLab Recruitment Team
""",
                settings.DEFAULT_FROM_EMAIL,
                [email],
                fail_silently=False,
            )

            messages.success(
                request,
                _("Your application has been submitted successfully.")
            )

        except Exception as e:
            messages.error(request, f"Email error: {e}")

        return redirect("careers")

    return render(request, "main/careers.html")


def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")
        consent = request.POST.get("consent")

        try:
            send_mail(
                f"New Contact Message - {subject}",
                f"""
New contact message received.

Name: {name}
Email: {email}
Subject: {subject}
Consent: {consent}

Message:
{message}
""",
                settings.DEFAULT_FROM_EMAIL,
                ["info@solutionstestlab.com"],
                fail_silently=False,
            )

            send_mail(
                "Message Received | SolutionsTestLab",
                f"""
Dear {name},

Thank you for contacting SolutionsTestLab.

We have successfully received your message regarding:

{subject}

Our team will review your inquiry and get back to you shortly.

Best regards,
SolutionsTestLab Team
""",
                settings.DEFAULT_FROM_EMAIL,
                [email],
                fail_silently=False,
            )

            messages.success(
                request,
                _("Your message was sent successfully.")
            )

        except Exception as e:
            messages.error(request, f"Email error: {e}")

        return redirect("contact")

    return render(request, "main/contact.html")


def impressum(request):
    return render(request, "main/impressum.html")


def privacy_policy(request):
    return render(request, "main/privacy_policy.html")


def blog(request):
    return render(request, "main/blog.html")


def blog_software_testing(request):
    return render(request, "main/blog_software_testing.html")