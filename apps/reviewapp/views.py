from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from .models import Review
from ..logregapp .models import User
from ..bookapp .models import Book

def create(request):
    print 'in the create method of reviews'
    new_rev = Review.objects.addMOREreviews(request.POST)
    id = request.POST['book_id']
    print 'new_rev =--->', new_rev
    print id
    return redirect('bookapp:info', id=id)

def delete(request, id):
    print 'in the DELETE method of reviews'
    Review.objects.filter(id=id).delete()
    print 'Rev bye'
    id = request.session['book_id']
    print ' book id', id
    return redirect('bookapp:info', id=id)

def users(request, id):
    context = {
    'totalReview': Review.objects.filter(reviewer=id),
    'totalReviewlen': len(Review.objects.filter(reviewer=id)),
    'currentUser': User.objects.filter(id=id),
    }
    return render(request, 'reviewapp/users.html', context)
