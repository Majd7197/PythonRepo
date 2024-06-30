from django.urls import path
from . import views

urlpatterns = [
    path('', views.root),  # This will handle the root URL
    path('blogs/', views.index),  # This will handle the 'blogs' URL
    path('blogs/new/', views.new),
    path('blogs/<int:number>/', views.show),
    path('blogs/<int:number>/edit/', views.edit),
    path('blogs/<int:number>/delete/', views.destroy),
    path('blogs/json/', views.blogs_json),
]
