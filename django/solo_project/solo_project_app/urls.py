from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='home'),  
    path('users',views.index),
    path('subscriptions',views.subscriptions),
    path('add_subscription/<int:id>',views.add_subscription),
    path('classes',views.classes),
    path('add_class',views.add_class),

]