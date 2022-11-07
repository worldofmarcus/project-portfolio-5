from django.shortcuts import render


def profile(request):
    """This method displays the users profile"""

    template = 'profiles/profile.html'
    context = {}

    return render(request, template, context)
