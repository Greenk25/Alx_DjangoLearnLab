
2. **Retrieve Operation:**

Create a Python script named `retrieve_book.py` to perform the retrieve operation:
```python3
# retrieve_book.py

from bookshelf.models import Book

# Retrieve the book you just created
book = Book.objects.get(title="1984")
print(book.title, book.author, book.publication_year)

