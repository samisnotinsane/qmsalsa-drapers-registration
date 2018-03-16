from django.urls import path

from . import views

urlpatterns = [
    path('', views.guest_list, name='guest_list'),
    path('register/', views.register_new, name='register_new'),
]