from django.db import models
from django.utils.text import slugify


class Profile(models.Model):
    name = models.CharField(max_length=120, default="Your Name")
    profession = models.CharField(max_length=120, default="IT Engineer")
    short_bio = models.TextField(blank=True)
    long_bio = models.TextField(blank=True)
    profile_image = models.ImageField(upload_to="profile/", blank=True, null=True)
    resume = models.FileField(upload_to="resume/", blank=True, null=True)
    email = models.EmailField(blank=True)
    location = models.CharField(max_length=120, blank=True)
    github_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)
    website_url = models.URLField(blank=True)

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profile"

    def __str__(self):
        return self.name


class Skill(models.Model):
    name = models.CharField(max_length=100)
    level = models.PositiveIntegerField(default=80, help_text="Percentage 0-100 for simple bars")
    category = models.CharField(max_length=100, blank=True)

    class Meta:
        ordering = ["-level", "name"]

    def __str__(self):
        return self.name