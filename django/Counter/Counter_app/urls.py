from django.urls import path
from . import views
urlpatterns = [
    path('',views.index),
    path('destroy_session',views.destroy_session),
    path('counter_two',views.counter_two),
    path('counter_by_any',views.counter_by_any),
]
