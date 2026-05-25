from django.contrib import admin

from .models import Job


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'location', 'job_type', 'status', 'posted_at')
    list_filter = ('status', 'job_type', 'is_remote', 'posted_at')
    search_fields = ('title', 'description', 'location')
    autocomplete_fields = ('company',)