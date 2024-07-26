from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('book_add',views.book_add),
    path('books/<int:id>/',views.views_books),
    path('authors',views.show_authors),
    path('author_add',views.add_authors),
    path('authors/<int:id>/',views.show_author),
    path('add_book_to_author',views.add_book_to_author),
]