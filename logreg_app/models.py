from django.db import models
import re

class UserManager(models.Manager):


    def basic_validator(self, post_data):
        errors = {}
        
        if len(post_data['first_name']) < 2 or len(post_data['first_name']) > 30:
            errors['first_name'] = "First name must be between 2 and 30 characters long."
        
        if len(post_data['last_name']) < 2 or len(post_data['last_name']) > 30:
            errors['last_name'] = "Last name must be between 2 and 30 characters long."
        
        if len(post_data['email']) < 3 or len(post_data['email']) > 30:
            errors['email'] = 'Email must be between 3 and 30 characters long.'

        try:
            User.objects.get(email = post_data['email'])
            errors['email_unique'] = 'This Email is already in use.'
        except:
            pass 

        
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

        if not EMAIL_REGEX.match(post_data['email']):
            errors['email_no'] = 'Not a vailid email format'

        if len(post_data['password']) < 8:
            errors['password_length'] = 'Password must be at least eight characters'
        
        if post_data['password'] != post_data['confirm_password']:
        
            errors['password_match'] = 'Password and confirm password must match.'


        return errors


class User(models.Model):
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    email = models.CharField(max_length = 30)
    password = models.CharField(max_length = 60)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()