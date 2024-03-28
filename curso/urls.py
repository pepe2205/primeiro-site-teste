from django.urls import path
from . import views

urlpatterns = [
    path('', views.curso_list, name='curso_list'),
]