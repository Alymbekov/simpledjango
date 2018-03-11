from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('', views.generic, name='generic'),
    path('', views.elements, name='elements'),
]
