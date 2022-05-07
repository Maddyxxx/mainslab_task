from django.contrib import admin
from .models import Client, Organization


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['client_name']


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ['client', 'organization_name']

