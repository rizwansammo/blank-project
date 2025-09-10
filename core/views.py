from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Profile, Skill
from .forms import ContactForm


def home(request):
    profile = Profile.objects.first()
    skills = Skill.objects.all()
    return render(request, "core/home.html", {"profile": profile, "skills": skills})


def about(request):
    profile = Profile.objects.first()
    skills = Skill.objects.all()
    return render(request, "core/about.html", {"profile": profile, "skills": skills})


def contact(request):
    profile = Profile.objects.first()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            message = form.cleaned_data["message"]

            subject = f"Portfolio Contact from {name}"
            body = f"From: {name} <{email}>\n\n{message}"
            recipient = profile.email or settings.DEFAULT_FROM_EMAIL
            if recipient:
                send_mail(subject, body, settings.DEFAULT_FROM_EMAIL, [recipient], fail_silently=False)
                messages.success(request, "Your message has been sent.")
                return redirect("contact")
            else:
                messages.error(request, "Email is not configured.")
    else:
        form = ContactForm()
    return render(request, "core/contact.html", {"form": form, "profile": profile})