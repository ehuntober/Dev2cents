from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.shortcuts import render, redirect

from users.decorators import login_excluded
from users.forms import ProfileForm
from users.models import Profile


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
            return redirect("homepage")
        else:
            messages.error(request, "Error logging in")
            return render(request, "users/login.html")
    else:
        return render(request, "users/login.html")


@login_required(login_url="login")
def logout_view(request):
    logout(request)
    messages.info(request, "Successfully logged out")
    return redirect("homepage")


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
            return render(request, "users/signup.html")

        # Attempt to create new user
        try:
            # adding first name and last name using extra_fields to the User fields
            extra_fields = {**extra_fields, "first_name": first_name, "last_name": last_name}
            user = User.objects.create_user(username, email, password, **extra_fields)
            user.save()
            messages.success(request, "User account created successfully")
        except IntegrityError:
            messages.info(request, "Username has already been taken")
            return render(request, "users/signup.html")
        login(request, user)
        messages.success(request, "Logged in successfully")
        return redirect("edit_account")
    else:
        return render(request, "users/signup.html")


@login_required(login_url="login")
def user_account(request):
    profile = request.user.profile
    if profile is None:
        messages.error(request, "User profile does not exist")
        return render(request, "error-page.html")
    context = {"user_profile": profile}
    return render(request, "users/profile.html", context)


@login_required(login_url="login")
def edit_account(request):
    user_account_profile = request.user.profile
    profile_form = ProfileForm(instance=user_account_profile)

    if request.method == "POST":
        profile_form = ProfileForm(request.POST, request.FILES, instance=user_account_profile)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, "Profile edited successfully")
            return redirect('create_cents')
    context = {"profile_form": profile_form, "profile": user_account_profile}
    return render(request, "users/edit-profile.html", context)


@login_required(login_url="login")
def user_profile(request, pk):
    profile = Profile.objects.get(id=pk)
    context = {"profile": profile}
    return render(request, "users/user-profile.html", context)
