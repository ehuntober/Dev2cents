from django.urls import path 

from . import views


urlpatterns = [
    path('feeds',views.cents_feed, name='cents_feed'),
    path('create_2cents',views.create_cents,name='create_cents'),
    path('create_profile',views.create_profile,name='create_profile'),
    path('profile',views.profile,name='profile')
]