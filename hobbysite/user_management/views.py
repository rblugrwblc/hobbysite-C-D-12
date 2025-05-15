from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import ProfileForm
from .models import Profile

@login_required
def update_profile(request):
    # ensure profile exists
    profile, created = Profile.objects.get_or_create(user=request.user, defaults={
        'email': request.user.email,
        'name': request.user.username,
    })

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            update_profile = form.save()
            return redirect('/profile')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'user_management/profile_form.html', {'form': form})
