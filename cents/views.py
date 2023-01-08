from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from cents.forms import CentsForm
from cents.models import Cent, Like
from users.forms import NewsletterForm
from users.models import Profile


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


def like(request, cent_id):
    if request.method == "POST":
        # make sure the user can't like more than one post
        user = User.objects.get(username=request.user.username)
        # find whatever cent is associated with like
        cent = Cent.objects.get(id=cent_id)

        new_like = Like(owner=user, cent=cent)
        new_like.already_liked = True

        cent.hearts += 1
        # adds user to cent
        cent.user_likes.add(user)
        cent.save()
        new_like.save()

        # Get all cents
        cents = Cent.objects.all()

        context = {"user": user, "cent": cent, "cents": cents}
        return render(request, "cents/cents-feed.html", context)


def dislike(request, cent_id):
    if request.method == "POST":
        # make sure the user can't like more than one post
        user = User.objects.get(username=request.user.username)
        # find whatever cent is associated with like
        cent = Cent.objects.get(id=cent_id)

        new_like = Like(owner=user, cent=cent)
        new_like.already_liked = False

        cent.hearts -= 1
        # removes user to cent
        cent.user_likes.remove(user)
        cent.save()
        new_like.save()

        # Get all cents
        cents = Cent.objects.all()

        context = {"user": user, "cent": cent, "cents": cents}
        return render(request, "cents/cents-feed.html", context)
