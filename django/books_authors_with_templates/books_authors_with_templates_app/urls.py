from django.urls import path
from . import views

urlpatterns = [
   # path('admin/', admin.site.urls),
   path('',views.index),
   path('add_book',views.add_book),
   path('books/<int:id>/',views.get_book),
   path('authors',views.display_authors),
   path('add_author',views.add_author),
   path('author/<int:id>/',views.get_author,name = 'author_details'),
   path('add_book_to_author', views.add_book_to_author, name='add_book_to_author'),
   path('add_author_to_book', views.add_author_to_book, name='add_author_to_book'),
]
