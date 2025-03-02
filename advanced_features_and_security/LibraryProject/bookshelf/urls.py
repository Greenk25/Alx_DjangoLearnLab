from django.urls import path
from .views import list_books, add_book, edit_book, delete_book, view_book, create_book

urlpatterns = [
    path('list/', list_books, name='list_books'),
    path('add/', add_book, name='add_book'),
    path('edit/<int:book_id>/', edit_book, name='edit_book'),
    path('delete/<int:book_id>/', delete_book, name='delete_book'),
]

