from django.urls import path

from users import views

urlpatterns = [
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("register/", views.register, name="register"),
    path("user-profile/", views.user_account, name="user_profile"),
    path("edit-profile/", views.edit_account, name="edit_profile"),
]
