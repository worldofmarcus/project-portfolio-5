from django.shortcuts import render


def privacy_policy(request):
    """
    This view renders the privacy page
    """
    return render(request, 'home/privacy_policy.html')


def faq(request):
    """
    This view renders the faq page
    """
    return render(request, 'home/faq.html')
