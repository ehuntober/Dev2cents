from django.urls import path 
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('login',views.login,name='login'),
    path('signup',views.signup,name='signup')
]

urlpatterns += staticfiles_urlpatterns()
