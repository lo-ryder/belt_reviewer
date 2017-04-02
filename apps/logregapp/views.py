from django.shortcuts import render, HttpResponse, redirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from .models import User, UserManager
# Create your views here.
def index(request):
    return render(request, 'logregapp/index.html')

def register(request):
    print "Success TYPE------------->", request.POST

    if request.method == "POST":
        print "~~~~in reg successful post~~~~~"

        valid, response = User.objects.register(request.POST)

        if valid:
            print "valid REGISTRATION-------->", response

            context = {
            'users': response, #new user from new_obj
            'type': 'registered',
            }
            print 'context obj---->',context['users']
            return render(request, 'logregapp/success.html',context)
        else:
            print "else error.....",response
            for error in response:
                print '......',error
            messages.error(request, response)
            return reverse('logregapp:index')
    if request.method == "GET":
        # return redirect(reverse('courses:courses'))
        return reverse('logregapp:index')

def login(request):
    print "Success TYPE.....>", request.POST
    print request.method

    if request.method == "POST":
        print "in login successful post"

        valid, response = User.objects.login(request.POST)

        if valid:
            print '+++++++valid login +++++++++', response
            for item in response:
                print 'Valid ID', item['id']
                request.session['id']= item['id']
                print 'session ID.......', request.session['id']
            context = {
            'users': response, #user found from email if password matched
            'type': 'logged in',
            }
            return redirect('bookapp:home')
        else:
            print ".......LOGIN else error.....",response

            for error in response:
                print '......',error
            messages.error(request, response)
            return redirect(reverse('logregapp:index'))

# Create your views here.
