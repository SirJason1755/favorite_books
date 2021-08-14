from django.urls import path     
from . import views
urlpatterns = [
        path('', views.index),
        path('users/registration',views.register),
        path('users/login',views.login),
        path('destroy',views.destroy),
]     