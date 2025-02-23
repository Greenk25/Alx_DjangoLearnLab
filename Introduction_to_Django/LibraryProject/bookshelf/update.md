
3. **Update Operation:**

Create a Python script named `update_book.py` to perform the update operation:
```python
# update_book.py

from bookshelf.models import Book

# Retrieve the book you just created
book = Book.objects.get(title="1984")

# Update the title of "1984" to "Nineteen Eighty-Four"
book.title = "Nineteen Eighty-Four"
book.save()
print(book.title)

