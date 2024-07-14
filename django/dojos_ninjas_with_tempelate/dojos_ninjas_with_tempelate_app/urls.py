from django.urls import path
from . import views
urlpatterns =[
    path('',views.index),
    path('dojo_add',views.dojo_add),
    path('ninja_add',views.ninja_add),
]