from django.shortcuts import render

# Create your views here.


def cents_feed(request):
    return render(request, 'cents/centsfeed.html')

def create_cents(request):
    return render(request, 'cents/create_cents.html')

def create_profile(request):
    return render(request, 'cents/create_profile.html')


def profile(request):
    return render(request,'cents/profile.html')
