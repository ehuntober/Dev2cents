from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.shortcuts import render, redirect

from users.decorators import login_excluded


# Create your views here.

@login_excluded(redirect_to="")
def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            messages.success(request, "Logged in successfully")
            return redirect("")
        else:
            messages.error(request, "Error logging in")
            return render(request, "")
    else:
        return render(request, "")


@login_required(login_url="login")
def logout_view(request):
    logout(request)
    messages.info(request, "Successfully logged out")
    return redirect("")


@login_excluded(redirect_to="home")
def register(request, **extra_fields):
    if request.method == "POST":
        first_name = request.POST["first-name"]
        last_name = request.POST["last-name"]
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            messages.error(request, "Passwords don't match")
            return render(request, "")

        # Attempt to create new user
        try:
            # adding first name and last name using extra_fields to the User fields
            extra_fields = {**extra_fields, "first_name": first_name, "last_name": last_name}
            user = User.objects.create_user(username, email, password, **extra_fields)
            user.save()
        except IntegrityError:
            messages.info(request, "Username has already been taken")
            return render(request, "")
        login(request, user)
        messages.success(request, "Logged in successfully")
        return redirect("")
    else:
        return render(request, "")
