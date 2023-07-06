from django.contrib import admin
from .models import Company, Administrator

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'sales_balance', 'inventory_balance')

@admin.register(Administrator)
class AdministratorAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'company')