from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('registration',views.index),
    path('login',views.login),
    path('success',views.success)
]