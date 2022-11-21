from django.shortcuts import render


def privacy_policy(request):
    return render(request, 'home/privacy_policy.html')


def faq(request):
    return render(request, 'home/faq.html')
