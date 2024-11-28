from django.urls import path

from newapp import views

urlpatterns = [
    path('', views.course_list, name='course_list'),
    path('delete/<int:course_id>/', views.delete_course, name='delete_course'),
]