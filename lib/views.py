from django.shortcuts import render, reverse
from . import models

def index(request):
    num_book = models.Book.objects.all().count()
    num_author = models.Author.objects.all().count()
    num_available = models.BookInstance.objects.all().count()
    num_available = models.BookInstance.objects.filter(status__exact='a').count()

    return render(request, 'lib/index.html',
        context={'num_books':num_book, 'num_authors':num_author, 'num_availables':num_available}
    )
