from django.urls import path, include
from . import views

my_app='lib'

urlpatterns = [
    path('', views.index, name='index'),
]
