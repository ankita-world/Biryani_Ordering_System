from django.contrib import admin
from .models import Biryani_Type, Biryani
# Register your models here.

@admin.register(Biryani_Type)
class BTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(Biryani)
class BAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'biryani_Type']
