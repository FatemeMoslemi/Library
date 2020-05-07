from django.urls import path, include
from . import views

my_app='lib'

urlpatterns = [
    path('', views.index, name='index'),
    path('books', views.BookListView.as_view(), name='books_list'),
    path('authors', views.AuthorListView.as_view(), name='authors_list'),
]
