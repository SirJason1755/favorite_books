from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from . models import Book
from logreg_app.models import User
import bcrypt

# Create your views here.
def index(request):
    if 'user_id' not in request.session:
        messages.error(request, 'Please log in to view this page')
        return redirect('/')

    context = {
        'user': User.objects.get(id= request.session['user_id']),
        'books': Book.objects.all(),
    }
    return render (request,'books.html',context)



def createbook(request):

    errors = Book.objects.basic_validator(request.POST)
    if errors:
        for k , v in errors.items():
            messages.error(request, v)
        return redirect('/favorite')


    Book.objects.create(
        title = request.POST['title'],
        description = request.POST['description'],
        user = User.objects.get(id= request.session['user_id'])
    )
    messages.info(request,'book created')

    return redirect('/favorite')


def viewbook(request, book_id):
    if 'user_id' not in request.session:
        return redirect('/')

    context = {
        'user': User.objects.get(id= request.session['user_id']),
        'book': Book.objects.get(id = book_id),
        
    }
    return render(request,'viewbook.html',context)


def update(request,book_id):
    book_update = Book.objects.get(id= book_id)
    book_update.title = request.POST['title']
    book_update.description = request.POST['description']
    book_update.save()
    return redirect(f"/favorite/books/{book_id}/view")


def delete(request,book_id):
    book_delete = Book.objects.get(id = book_id)
    book_delete.delete()

    return redirect("/favorite")

def like(request,book_id):
    user = User.objects.get(id= request.session['user_id'])
    add_book = Book.objects.get(id= book_id)
    user.favorite_book.add(add_book)
    return redirect(f'/favorite/books/{book_id}/view')

def unlike(request,book_id):
    user = User.objects.get(id= request.session['user_id'])
    delete_book = Book.objects.get(id= book_id)
    user.favorite_book.remove(delete_book)
    return redirect(f'/favorite/books/{book_id}/view')