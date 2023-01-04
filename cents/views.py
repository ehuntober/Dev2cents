from django.shortcuts import render

# Create your views here.


def cents_feed(request):
    return render(request, 'cents/centsfeed.html')
