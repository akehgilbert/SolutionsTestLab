from django.contrib import admin
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _
from .models import ContactInquiry, JobApplication

@admin.register(ContactInquiry)
class ContactInquiryAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject', 'created_at', 'is_processed')
    list_filter = ('subject', 'is_processed', 'created_at')
    search_fields = ('name', 'email', 'message')
    list_editable = ('is_processed',)
    ordering = ('-created_at',)

@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    # What to show in the main table list
    list_display = ('full_name', 'position', 'status', 'applied_at', 'download_resume')
    
    # Filters on the right side
    list_filter = ('position', 'status', 'applied_at')
    
    # Fields editable directly in the list
    list_editable = ('status',)
    
    # Search functionality
    search_fields = ('full_name', 'email', 'cover_letter', 'internal_notes')
    
    # Organizing the detail view (when you click on an application)
    fieldsets = (
        (_('Candidate Information'), {
            'fields': ('full_name', 'email', 'position', 'applied_at')
        }),
        (_('Application Content'), {
            'fields': ('cover_letter', 'resume')
        }),
        (_('Internal Management'), {
            'fields': ('status', 'internal_notes'),
            'description': _("Update the status and add notes for the team here.")
        }),
    )
    
    readonly_fields = ('applied_at',)
    ordering = ('-applied_at',)

    # The custom download link helper
    def download_resume(self, obj):
        if obj.resume:
            return format_html(
                '<a href="{}" target="_blank" style="font-weight:bold; color:#0056b3;">'
                '📄 Open CV</a>', 
                obj.resume.url
            )
        return _("No File")
    
    download_resume.short_description = _("Resume")