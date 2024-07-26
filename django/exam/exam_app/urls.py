from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('registration',views.index),
    path('login',views.login),
    path('dashboard',views.success),
    path('logout',views.logout),
    path('add_pie',views.add_pie),
    path('pies/edit/<int:id>',views.edit_pie),
    path('update_pie',views.update_pie),
    path('delete/<int:id>',views.delete_pie),
    path('pies',views.show_all_pies),
    path('pies/<int:id>',views.view_pie),
    
]