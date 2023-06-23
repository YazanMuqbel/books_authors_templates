from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    #authors = models.ManyToManyField(Author, related_name='books')

    def __str__(self):
        return self.title

class Author(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    notes = models.TextField(blank=True)
    books = models.ManyToManyField(Book, related_name='authors')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    

    