from .models import Profile

def site_profile(request):
    return {"site_profile": Profile.objects.first()}