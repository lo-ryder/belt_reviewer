from __future__ import unicode_literals

from django.db import models
# from ..logregapp .models import User
# from ..reviewapp .models import Review

class AuthorManager(models.Manager):

    def addauthor(self, postData):
        print 'Add Author: POST DATA------> ', postData

        new_author = Author.objects.create(
        name = postData['authorinput'],
        )
        # new_Aid = new_author['id']
        print 'NEW Author------>>> ', new_author

        new_book = Book.objects.create(
        title = postData['title'],
        author = new_author,
        )

        print 'NEW BOOK------>>> ', new_book

        new_id = Book.objects.filter(title=postData['title']).values()

        return new_author, new_id


class BookManager(models.Manager):

    def createbook(self, postData):
        print 'Create Book: POST DATA------> ', postData

        new_book = Book.objects.create(
        title = postData['title'],
        author = Author.objects.get(id=postData['author'])
        )
        new_id = Book.objects.filter(title=postData['title']).values()
        print 'old author buuuuuuutt NEW BOOK------>>> ', new_book
        print 'my new book has a new id------>>> ', new_id
        return new_id


# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = AuthorManager()

class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(Author, related_name='books')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = BookManager()
