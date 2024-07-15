from django.urls import path
from . import views

urlpatterns = [
   # path('admin/', admin.site.urls),
   path('',views.index),
   path('add_book',views.add_book),
]
