from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('number_guess/', views.number_guess, name='number_guess'),  # Ensure the URL pattern ends with a slash
    path('reset/', views.reset, name='reset'),
]
