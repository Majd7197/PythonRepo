from django.urls import path
from . import views
urlpatterns = [
    path('',views.index),
    path('subscriptions',views.subscriptions),
    path('add_subscription/<int:id>',views.add_subscription),

]