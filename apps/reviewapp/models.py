from __future__ import unicode_literals

from django.db import models
from ..logregapp .models import User
from ..bookapp .models import Book

class ReviewManager(models.Manager):

    def addreview(self, postData):
        print 'Add Review: POST DATA------> ', postData

        new_rev = Review.objects.create(
        content = postData['content'],
        rating = postData['rating'],
        book_reviewed = Book.objects.get(title=postData['title']),
        reviewer = User.objects.get(id=postData['user_id']),
        )

        print 'NEW Review-from add book & review page ----->>> ', new_rev
        return new_rev

    def addMOREreviews(self, postData):
        print 'Add MOREEEEEE Reviews: POST DATA------> ', postData

        new_rev = Review.objects.create(
        content = postData['content'],
        rating = postData['rating'],
        book_reviewed = Book.objects.get(id=postData['book_id']),
        reviewer = User.objects.get(id=postData['user_id']),
        )

        print 'NEW Review-from JUST review page ----->>> ', new_rev
        return new_rev


class Review(models.Model):
    content = models.CharField(max_length=200)
    rating = models.IntegerField()
    book_reviewed = models.ForeignKey(Book, related_name='review_for_book')
    reviewer = models.ForeignKey(User, related_name='content_written')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = ReviewManager()
