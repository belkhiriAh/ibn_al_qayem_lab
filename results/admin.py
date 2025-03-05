from django.contrib import admin
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _
from .models import LabResult

# Register your models here.

@admin.register(LabResult)
class LabResultAdmin(admin.ModelAdmin):
    list_display = ('result_number', 'date_created', 'display_result_image', 'display_qr_code', 'display_password', 'is_active')
    list_filter = ('is_active', 'date_created')
    search_fields = ('result_number',)
    readonly_fields = ('result_number', 'qr_code', 'password')
    ordering = ('-date_created',)
    list_per_page = 20

    fieldsets = (
        (_('Result Information'), {
            'fields': ('result_number', 'password')
        }),
        (_('Result Details'), {
            'fields': ('result_image', 'is_active')
        }),
        (_('QR Code'), {
            'fields': ('qr_code',),
            'classes': ('collapse',)
        }),
    )

    def display_result_image(self, obj):
        if obj.result_image:
            return format_html(
                '<a href="{}" target="_blank"><img src="{}" width="50" height="50" style="object-fit: cover; border-radius: 5px;"/></a>',
                obj.result_image.url,
                obj.result_image.url
            )
        return "-"
    display_result_image.short_description = _('Result Image')

    def display_qr_code(self, obj):
        if obj.qr_code:
            return format_html(
                '<a href="{}" target="_blank"><img src="{}" width="50" height="50" style="object-fit: cover; border-radius: 5px;"/></a>',
                obj.qr_code.url,
                obj.qr_code.url
            )
        return "-"
    display_qr_code.short_description = _('QR Code')

    def display_password(self, obj):
        return format_html('<code style="background: #f8f9fa; padding: 4px 8px; border-radius: 4px;">{}</code>', obj.password)
    display_password.short_description = _('Password')

    def save_model(self, request, obj, form, change):
        if not change:  # Only set password for new objects
            obj.password = obj.generate_random_password()
        super().save_model(request, obj, form, change)
