from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from cents.models import Cent
from users.models import Profile
from users.forms import NewsletterForm
from cents.forms import CentsForm


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
    else:
        newsletter_form = NewsletterForm()
    context = {"newsletter_form": newsletter_form}
    return render(request, "index.html", context)


def cents_feed(request):
    cents = Cent.objects.all()
    context = {"cents": cents}
    return render(request, "cents/cents-feed.html", context)


@login_required(login_url="login")
def create_cents(request):
    owner = request.user
    if request.method == "POST":
        form = CentsForm(request.POST)
        if form.is_valid():
            cent_form = form.save(commit=False)
            cent_form.owner = owner
            cent_form.save()
            messages.success(request, "You have successfully created a 2cent")
            return redirect('cents_feed')
        else:
            messages.error(request, "Error creating 2cent")
    else:
        form = CentsForm()
    context = {"form": form}
    return render(request, "cents/create-cents.html", context)
