from django.contrib import admin
from .models import CustomUser , Profile

# Register your models here.

class ProfileInline(admin.TabularInline):
    extra = 0
    model = Profile

@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    inlines = [ProfileInline]
    list_display = ["email","username","is_active","is_staff"]
    search_fields = ["email","username"]
    list_filter = ["is_active","is_staff"]