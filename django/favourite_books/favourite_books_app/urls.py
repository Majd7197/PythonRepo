from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('registration',views.index),
    path('login',views.login),
    path('success',views.success),
    path('logout',views.logout),
    path('add_book',views.add_book),
    path('add_to_favourites/<int:id>',views.add_to_favourites),
]