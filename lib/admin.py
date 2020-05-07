from django.contrib import admin
from . import models

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'genre')

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'genre')
    fields = ['first_name', 'last_name', ('genre')]
