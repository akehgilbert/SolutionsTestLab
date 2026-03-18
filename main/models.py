from django.db import models
from django.utils.translation import gettext_lazy as _

class ContactInquiry(models.Model):
    SUBJECT_CHOICES = [
        ('Development', _('Software Development')),
        ('Testing', _('Software Testing / QA')),
        ('Partnership', _('General Partnership')),
        ('Careers', _('Career Inquiry')),
    ]

    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=50, choices=SUBJECT_CHOICES)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_processed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} - {self.subject} ({self.created_at.strftime('%Y-%m-%d')})"

    class Meta:
        verbose_name = _("Contact Inquiry")
        verbose_name_plural = _("Contact Inquiries")


class JobApplication(models.Model):
    POSITION_CHOICES = [
        ('QA', _('QA Automation Engineer')),
        ('Dev', _('Django Backend Developer')),
        ('Other', _('Open Application')),
    ]

    STATUS_CHOICES = [
        ('pending', _('Pending Review')),
        ('interview', _('Interview Scheduled')),
        ('rejected', _('Rejected')),
        ('hired', _('Hired')),
    ]

    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    position = models.CharField(max_length=50, choices=POSITION_CHOICES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    resume = models.FileField(upload_to='resumes/%Y/%m/')
    cover_letter = models.TextField(blank=True)
    
    # NEW: Internal notes for the team (not shown to the candidate)
    internal_notes = models.TextField(blank=True, verbose_name=_("Internal Team Notes"))
    
    applied_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.position} ({self.get_status_display()})"

    class Meta:
        verbose_name = _("Job Application")
        verbose_name_plural = _("Job Applications")