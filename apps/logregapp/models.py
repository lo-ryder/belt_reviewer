from __future__ import unicode_literals
import re
import bcrypt
from django.db import models


#Our new manager!
#No methods in our new manager should ever catch the whole request object with a parameter!!! (just parts, like request.POST)
class UserManager(models.Manager):
    print "In User Manager"

    def register(self, postData):
        errors = []
        emailck = postData['email']
        print emailck
        EMAIL_REGEX = re.match(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$', emailck)
        print EMAIL_REGEX

        if EMAIL_REGEX is None:
            errors.append('Email: Required. Valid format.')
        if len(postData['first_name'])<1:
            errors.append('First Name: No fewer than 2 characters; letters only.')

        if len(postData['last_name'])<1:
            errors.append('Last Name: No fewer than 2 characters; letters only.')

        if EMAIL_REGEX is None:
            errors.append('Email: Required. Valid format.')

        if len(postData['password'])<7 and postData['password'] == postData['con_password']:
            errors.append('Password: Required; No fewer than 8 characters in length; matches Password Confirmation')

        print errors

        if errors:
            return False, errors

        else:
            key = postData['password'].encode()
            hashed_key = bcrypt.hashpw(
                key,
                bcrypt.gensalt()
            )

            print "\n\n>>>>>>>>><<<<>>>><<<<>>><>**\n\nhash->", hashed_key

            new_obj = User.objects.create(
            user_alias = postData['user_alias'],
            first_name = postData['first_name'],
            last_name = postData['last_name'],
            email = postData['email'],
            password = hashed_key
            )

            find_user = User.objects.filter(email=postData['email']).values()

            return True, find_user

    def login(self, postData):
            errors = []
            print "In login........."

            find_user = User.objects.filter(email=postData['email']).values()
            print find_user

            for item in find_user:
                user_password = item['password']
                print "F I N D  U S E R . . . . ", item['password']

                key = postData['password'].encode()
                hashed_key = bcrypt.hashpw(
                    key,
                    item['password'].encode()
                )
                print hashed_key

            if user_password == hashed_key:
                print "password MATCH <<<<<<<<<<<"
                return True, find_user
            else:
                print "wrong username or password"
                errors.append('Login: user or password inccorrect')
                return False, errors



    def validate_activity(self, postData):
        print "in models", postData

        errors = []

        if len(postData['name'])<1:
            errors.append('No fewer than 2 characters; letters only.')

        # Location.objects.get(id=postData['location'])
class User(models.Model):
        user_alias = models.CharField(max_length=45)
        first_name = models.CharField(max_length=45)
        last_name = models.CharField(max_length=45)
        email = models.CharField(max_length=200)
        password = models.CharField(max_length=100)
        created_at = models.DateTimeField(auto_now_add = True)
        updated_at = models.DateTimeField(auto_now = True)

        objects = UserManager()
