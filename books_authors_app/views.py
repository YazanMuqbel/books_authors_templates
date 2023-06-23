from django.shortcuts import render, redirect
from django.urls import reverse
from books_authors_app.models import Book
from books_authors_app.models import Author

# Create your views here.

# This function takes the user to the main page where he can add a new book and also see all books added to db
def home(request):
    data = dict(
        books = Book.objects.all(),
    )
    return render(request, 'new_book.html', context=data)


# This function POSTS and adds a new book to the db when user clicks "ADD BOOK"
def add_book(request):
    if request.method == 'POST':
        params = dict()
        
        params['title'] = request.POST.get('title')
        params['description'] = request.POST.get('description')
        
        Book.objects.create(**params)

    return redirect(reverse('home'))


#This function displays information about a specific book (get by id) in a seprate HTML page called "display_book.html"
"""def display_book(request, id):
    book = Book.objects.get(id=id)
    context={
        'book': book
    }
    return render(request, 'display_book.html', context)"""

#This function displays information about a specific book (get by id) in a seprate HTML page called "display_book.html"
def display_book(request, book_id):
    book = Book.objects.get(pk=book_id)
    assigned_authors = book.authors.all()
    all_authors = Author.objects.all()
    return render(request, 'display_book.html', {'book': book, 'assigned_authors': assigned_authors, 'all_authors': all_authors})


# This function takes the user to the main page where he can add a new AUTHOR and also see all authors added to db
def home_authors(request):
    data = dict(
        authors = Author.objects.all(),
    )
    return render(request, 'new_author.html', context=data)


# This function POSTS and adds a new AUTHOR to the db when user clicks "ADD AUTHOR"
def add_author(request):
    if request.method == 'POST':
        params = dict()
        
        params['first_name'] = request.POST.get('first_name')
        params['last_name'] = request.POST.get('last_name')
        params['notes'] = request.POST.get('notes')
        
        Author.objects.create(**params)

    return redirect(reverse('home_authors'))

# This function displays information about a specific Author
def display_author(request, author_id):
    author = Author.objects.get(pk=author_id)
    assigned_books = author.books.all()
    all_books = Book.objects.all()

    return render(request, 'display_author.html', {'author': author , 'assigned_books': assigned_books , 'all_books': all_books})


# This function assigns/adds an existing author to an existing book from a dropdown list
def assign_author_to_book(request, book_id):
    author_id =request.POST['author']
    author = Author.objects.get(pk=int(author_id))
    book = Book.objects.get(pk=book_id)
    book.authors.add(author)
    return redirect('/books/' +str( book.id))

# This function assignd/add an existing book to an existing author from a dropdown list
def assign_book_to_author(request, author_id):
    book_id = request.POST['book']
    book = Book.objects.get(pk=int(book_id))
    author = Author.objects.get(pk=author_id)
    author.books.add(book)
    return redirect('/authors/' + str(author.id))

