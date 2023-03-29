from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import NewsletterSignupForm


def newsletter(request):
    """
    A view for the newsletter signup.
    """
    if request.method == 'POST':
        newsletter_form = NewsletterSignupForm(request.POST)
        if newsletter_form.is_valid():
            newsletter_form.save()
            messages.success(
                request, 'Your details have been added to our mailing list!')
        else:
            messages.error(
                request, 'An error occured! Your details were not added.')
    else:
        newsletter_form = NewsletterSignupForm()

    context = {
        'form': newsletter_form
    }

    return render(request, 'newsletter/newsletter.html', context)
