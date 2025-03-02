from django.shortcuts import render
from django.views.generic import DetailView
from .models import Library
from django.contrib.auth.decorators import permission_required
from .models import Book

def add_book(request):
    # Logic to add a book
    return render(request, 'add_book.html')
    pass

@permission_required('relationship_app.can_change_book')
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    # Logic to edit a book
    pass

@permission_required('relationship_app.can_delete_book')
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    # Logic to delete a book
    pass

def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'

# Create your views here.
