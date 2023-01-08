from django.urls import path

from users import views

urlpatterns = [
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("register/", views.register, name="register"),
    path("user-account/", views.user_account, name="user_account"),
    path("edit-account/", views.edit_account, name="edit_account"),
    path("profile/<str:pk>/", views.user_profile, name="user_profile")
]
