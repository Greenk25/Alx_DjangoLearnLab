from django.db import models
# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=255)  # Field to store the author's name

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=255)  # Field for the book title
    publication_year = models.IntegerField()  # Year the book was published
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

