from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('courses/destroy/<int:id>/', views.delete_course_page, name='delete_course_page'),
    path('do_not_delete_course', views.do_not_delete_course, name='do_not_delete_course'),
    path('delete_course',views.delete_course)
]
