from django.urls import path

from cents import views


urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('cents-feed/', views.cents_feed, name="cents_feed"),
    path('create-cents/', views.create_cents, name="create_cents"),
]