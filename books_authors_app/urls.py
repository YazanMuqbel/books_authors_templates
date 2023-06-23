from django.urls import path, reverse     
from . import views

urlpatterns = [
    #path('', views.view_book, name='view_book'),
    
    # this path takes user to the home page
    path('', views.home, name='home'),

    # this paths adds a new book to database using POST method
    path('add_book', views.add_book, name='add_book'),

    #This function takes the user to a new html page that shows info of a selected book
    path('books/<int:book_id>/', views.display_book, name='display_book'),

    # this path takes user to the home page of AUTHORS
    path('authors', views.home_authors, name='home_authors'),

    # this paths adds a new AUTHOR to database using POST method
    path('add_author', views.add_author, name='add_author'),

# this path takes user to a new html page that show info of a selected AUTHOR
    path('authors/<int:author_id>/', views.display_author, name='display_author'),

# this path assigns an existing author to an existing book from a dropdown list
    path('assign_author_book/<int:book_id>', views.assign_author_to_book , name='assign_author_to_book' ),

# this path assigns an existing book to an existing author from a dropdown list
    path('assign_book_author/<int:author_id>', views.assign_book_to_author, name='assign_book_to_author'),

    ]