from django.contrib import admin

from .models import Company


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'owner', 'created_at')
    list_filter = ('location', 'created_at')
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}