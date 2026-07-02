from django.contrib import messages
from django.shortcuts import render, redirect
from django.utils.translation import gettext as _
from django.core.mail import EmailMessage
from django.conf import settings
import traceback


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
        name = request.POST.get("name", "").strip()
        email = request.POST.get("email", "").strip()
        position = request.POST.get("position", "").strip()
        cover_letter = request.POST.get("cover_letter", "").strip()
        resume = request.FILES.get("resume")

        try:
            company_email = EmailMessage(
                subject=f"New Job Application - {position}",
                body=f"""
New job application received.

Name: {name}
Email: {email}
Position: {position}

Cover Letter:
{cover_letter}
""",
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=[settings.DEFAULT_FROM_EMAIL],
                reply_to=[email] if email else None,
            )

            if resume:
                company_email.attach(
                    resume.name,
                    resume.read(),
                    resume.content_type
                )

            company_email.send(fail_silently=False)

            messages.success(
                request,
                _("Your application has been submitted successfully.")
            )

        except Exception:
            print(traceback.format_exc())
            messages.error(
                request,
                _("Email error. Please try again later or contact us directly.")
            )

        return redirect("careers")

    return render(request, "main/careers.html")


def contact(request):
    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        email = request.POST.get("email", "").strip()
        subject = request.POST.get("subject", "").strip()
        message = request.POST.get("message", "").strip()
        consent = request.POST.get("consent", "")

        try:
            contact_email = EmailMessage(
                subject=f"New Contact Message - {subject}",
                body=f"""
New contact message received.

Name: {name}
Email: {email}
Subject: {subject}
Consent: {consent}

Message:
{message}
""",
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=[settings.DEFAULT_FROM_EMAIL],
                reply_to=[email] if email else None,
            )

            print("EMAIL_HOST_USER =", repr(settings.EMAIL_HOST_USER))
            print("EMAIL_HOST_PASSWORD =", repr(settings.EMAIL_HOST_PASSWORD))
            print("DEFAULT_FROM_EMAIL =", repr(settings.DEFAULT_FROM_EMAIL))

            contact_email.send(fail_silently=False)

            messages.success(
                request,
                _("Your message was sent successfully.")
            )

        except Exception:
            print(traceback.format_exc())
            messages.error(
                request,
                _("Email error. Please try again later or contact us directly.")
            )

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