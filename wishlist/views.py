from django.shortcuts import render


def wishlist(request):
    """
    A view to show the user wishlist
    """

    return render(request, 'wishlist/wishlist.html')
