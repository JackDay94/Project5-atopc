from django.shortcuts import render, get_object_or_404
from .models import Profile
from .forms import ProfileForm
from django.views.generic import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages


class ProfileView(LoginRequiredMixin, UpdateView):
    """
    Checks the user is logged in and displays the user profile
    and allows them to update it with fields from the ProfileForm.
    Displays a success message when they update successfully or returns
    an error message when the form is invalid.
    """
    model = Profile
    form_class = ProfileForm
    template_name = "profiles/profile.html"
    success_message = "Your profile has been updated successfully!"
    error_message = "An error occured. Please check the form is valid!"

    def get_success_url(self):
        messages.success(self.request, self.success_message)
        return reverse_lazy("profile", kwargs={"pk": self.object.id})

    def form_invalid(self, form):
        messages.error(self.request, self.error_message)
