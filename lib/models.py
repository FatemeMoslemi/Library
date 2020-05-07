from django.db import models
from django.urls import reverse
import uuid

#Details of eveey genre.
class Genre(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('genre-detail', args=[str(self.id)])


#Details of eveey book.
class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    genre = models.ManyToManyField(Genre)
    price = models.IntegerField(default=0)
    isbn = models.CharField('ISBN', max_length=13, help_text='<a href="https://isbn_internation.org">13 characters<a/>')

    def __str__(self):
        return '%s %s' % self.title, self.genre

        def get_absolute_url(self):
            return reverse('book-detail', args=[str(self.id)])


class BookInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)
    due_back = models.DateField(null=True, blank=True)

    loan_status = (
        ('a','Available'),
        ('n','Not Available'),
    )

    status = models.CharField(max_length=1, choices=loan_status, default='a', blank=True)

    class Meta:
        ordering = ['due_back']

    def __str__(self):
        return '%s %s' % (self.id, self.book.title)

#Details of eveey author.
class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    genre = models.ManyToManyField(Genre)

    def __str__(self):
        return '%s %s' % self.first_name, self.last_name

    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])
