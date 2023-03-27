from django.shortcuts import render, get_object_or_404
from .models import Profile
from .forms import ProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required
def profile(request):
    """
    A view to show the User profile
    Credit : Code Institutes Boutique Ado project
    """
    profile = get_object_or_404(Profile, user=request.user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
        else:
            messages.error(
                request, 'Update failed! Please check the form is valid.'
                )
    else:
        form = ProfileForm(instance=profile)

    form = ProfileForm(instance=profile)

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'on_profile_page': True
    }

    return render(request, template, context)
