from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from cents.models import Cent
from users.forms import NewsletterForm


# Create your views here.


def homepage(request):
    if request.method == "POST":
        newsletter_form = NewsletterForm(request.POST)
        if newsletter_form.is_valid():
            newsletter_form.clean()
            newsletter_form.save()
            messages.success(request, "You have successfully signed up for the newsletter")
        else:
            messages.info(request, "You have already signed up for the newsletter")
    newsletter_form = NewsletterForm()
    context = {"newsletter_form": newsletter_form}
    return render(request, "index.html", context)


def cents_feed(request):
    cents = Cent.objects.all()
    context = {"cents": cents}
    return render(request, "cents/cents-feed.html")


@login_required(login_url="login")
def create_cents(request):
    return render(request, "cents/create-cents.html")
