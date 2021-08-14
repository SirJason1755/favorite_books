from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('books',views.createbook),
    path('books/<int:book_id>/view',views.viewbook),
    path('books/<int:book_id>/update',views.update),
    path('books/<int:book_id>/delete',views.delete),
    path('books/<int:book_id>/like',views.like),
    path('books/<int:book_id>/unlike',views.unlike)
    
]