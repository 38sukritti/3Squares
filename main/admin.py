import csv
from django.contrib import admin
from django.http import HttpResponse
from .models import Inquiry

@admin.action(description="Export selected inquiries to CSV")
def export_inquiries_csv(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="inquiries.csv"'
    writer = csv.writer(response)
    
    # Write Header
    writer.writerow(['Name', 'Phone', 'Email', 'Project Type', 'Message', 'Date Received'])
    
    # Write Data
    for inquiry in queryset:
        writer.writerow([
            inquiry.name,
            inquiry.phone,
            inquiry.email,
            inquiry.project_type,
            inquiry.message,
            inquiry.created_at.strftime("%Y-%m-%d %H:%M:%S")
        ])
    
    return response

@admin.register(Inquiry)
class InquiryAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'project_type', 'created_at')
    list_filter = ('project_type', 'created_at')
    search_fields = ('name', 'phone', 'email')
    ordering = ('-created_at',)
    actions = [export_inquiries_csv]

    # Making the view cleaner
    fieldsets = (
        ('Contact Information', {
            'fields': ('name', 'phone', 'email')
        }),
        ('Project Details', {
            'fields': ('project_type', 'message')
        }),
        ('Metadata', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )
    readonly_fields = ('created_at',)

    class Media:
        css = {
            'all': ('main/css/admin_custom.css',)
        }
