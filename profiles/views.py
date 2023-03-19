from django.shortcuts import render, get_object_or_404
from .models import Profile
from .forms import ProfileForm
from django.views.generic import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


class ProfileView(LoginRequiredMixin, UpdateView):
    """
    Checks the user is logged in and displays the user profile
    and allows them to update it with fields from the ProfileForm.
    Displays a success message when they update successfully.
    """
    model = Profile
    form_class = ProfileForm
    template_name = "profiles/profile.html"

    def get_success_url(self):
        return reverse_lazy("profile", kwargs={"pk": self.object.id})
