from django.urls import path 

from . import views


urlpatterns = [
    path('feeds',views.cents_feed, name='cents_feed'),
]