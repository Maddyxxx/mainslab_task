from django.contrib import admin
from .models import Bill


@admin.register(Bill)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['bill_number']


