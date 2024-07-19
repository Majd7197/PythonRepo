from django.urls import path
from . import views
urlpatterns = [
    path('shows/new',views.index),
    path('shows',views.shows),
    path('add_show',views.add_show),
    path('shows/<int:id>/',views.show_info),
    path('shows/<int:id>/destroy/',views.delete_show),
    path('shows/<int:id>/edit',views.edit_show_page),
    path('edit_show',views.edit_show),
    
]
