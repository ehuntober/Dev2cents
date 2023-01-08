from django.urls import path

from cents import views

urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('cents-feed/', views.cents_feed, name="cents_feed"),
    path('create-cents/', views.create_cents, name="create_cents"),
    path('cent/like/<str:cent_id>/', views.like, name="like"),
    path('cent/dislike/<str:cent_id>/', views.dislike, name="dislike"),
    path('top-cents/', views.top_cents, name="top_cents")
]
