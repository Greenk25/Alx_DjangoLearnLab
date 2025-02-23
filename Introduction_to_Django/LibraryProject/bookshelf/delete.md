
4. **Delete Operation:**

Create a Python script named `delete_book.py` to perform the delete operation:
```python
# delete_book.py

from bookshelf.models import Book

# Retrieve the book you just created
book = Book.objects.get(title="1984")

# Delete the book instance
book.delete()

# Confirm the deletion
books = Book.objects.all()
print(books)

