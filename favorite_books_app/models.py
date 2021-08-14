from django.db import models
from logreg_app.models import User

class BookManager(models.Manager):
# Create your models here.

    def basic_validator(self, post_data):
        errors = {}


        if len(post_data['title']) > 100 or len(post_data['title']) < 3:
            errors['title'] = 'title must be between 100 and 3 characters.'

        if len(post_data['description']) > 300 or len (post_data['description']) < 3:
            errors['description'] = 'quote must be between 30 and 30 characters'

        return errors


class Book(models.Model):
    title = models.CharField(max_length = 100)
    description = models.TextField(max_length = 300)
    user = models.ForeignKey(User,related_name = 'create_book', on_delete = models.CASCADE)
    favorite = models.ManyToManyField(User, related_name = 'favorite_book')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BookManager()