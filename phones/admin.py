from django.contrib import admin
from .models import Phone

# Register your models here.

@admin.register(Phone)
class Phone_Admin(admin.ModelAdmin):
    list_display = ('name', 'price', 'slug')
    prepopulated_fields = {"slug": ("name",)}