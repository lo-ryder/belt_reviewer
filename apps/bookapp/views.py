from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from .models import Book, Author
from ..logregapp .models import User
from ..reviewapp .models import Review

# Create your views here.
# urlpatterns = [
#     url(r'^books/add$', views.newbook, name='newbook'),
#     url(r'^books/(?P<id>\d+)$', views.info, name='info'),
#     url(r'^books$', views.home, name='home'),
# ]

def home(request):
    print '...................in bookapp:home'
    context = {
    'users': User.objects.all(),
    'books3': Book.objects.order_by("created_at").reverse()[:3],
    'booksMore': Book.objects.order_by("created_at").reverse()[3:],
    'reviews3': Review.objects.order_by("created_at").reverse()[:3],
    'reviewsMore': Review.objects.order_by("created_at").reverse()[3:],
    'currentUser': User.objects.filter(id=request.session['id']),
    }
    print 'current_user DATA is......', context['currentUser']
    return render(request, 'bookapp/home.html',context)

def info(request, id):
    context = {
    'authors': Author.objects.all(),
    'books': Book.objects.all(),
    'currentBook': Book.objects.filter(id=id),
    'reviews': Review.objects.all(),
    'currentReview': Review.objects.filter(book_reviewed__id=id),
    }
    request.session['book_id'] = id
    print '...................in bookapp:info'
    return render(request, 'bookapp/info.html',context)

def newbook(request):
    print '...................in bookapp:newbook'
    context = {
    'authors': Author.objects.all(),
    'books': Book.objects.all(),
    'reviews': Review.objects.all(),
    }
    print context['authors'], context['books'], context['reviews']
    if request.method =="POST":
        print 'views.newbook post method!!!!'

        if not request.POST['authorinput'] == " ":
            print '_______creating a new author!'

            requestinfo = request.POST
            new_author, info_id = Author.objects.addauthor(requestinfo)
            new_review = Review.objects.addreview(requestinfo)

            print ' NEW AUTHOR+++', new_author
            print 'new book ID++++', info_id
            print 'new REVIEW++++', new_review
            for item in info_id:
                print 'Valid ID', item['id']
                id = item['id']
            return redirect('bookapp:info', id=id)
        else:
            print '________<><><>creating a book and review for exsisting author!'

            requestinfo = request.POST
            info_id = Book.objects.createbook(requestinfo)
            print 'print check #1', info_id
            Review.objects.addreview(requestinfo)
            print 'print check x 2'*5
            for item in info_id:
                print 'Valid ID', item['id']
                id = item['id']
            return redirect('bookapp:info', id=id)
    else:
        return render(request, 'bookapp/newbook.html',context)
def newauthor(request):
    print '.....Creating new author'

    new_author, new_Aid = Author.objects.addauthor(request.POST)
    print ' NEW AUTHOR+++', new_author, 'w/ ID->', new_Aid
    return render(request, 'bookapp/newbook.html')
