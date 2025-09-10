from django.contrib import admin
from .models import Profile, Skill


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("name", "profession", "email")
    fieldsets = (
        (None, {"fields": ("name", "profession", "email", "location")}),
        ("Bios", {"fields": ("short_bio", "long_bio")}),
        ("Links", {"fields": ("github_url", "linkedin_url", "website_url")}),
        ("Media", {"fields": ("profile_image", "resume")}),
    )


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "level")
    list_filter = ("category",)
    search_fields = ("name", "category")