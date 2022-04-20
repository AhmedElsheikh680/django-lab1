from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
import os
import json
file = open(os.path.join(settings.BASE_DIR, 'static/books/books.json'))
books = json.load(file)

# books = [
#     {"id":"1", "name": "The Life"},
#     {"id":"2","name": "The Man"},
#     {"id":"3","name": "The Name"},
#     {"id":"4","name": "The Day"}
# ]


# Create your views here.




def index(request):
    context = {
        "books": books
    }
    return render(request, "books/index.html", context=context);


def show(request, book_id):
    show_book = book_search(books, book_id)
    print(show_book)

    context = {
        "book": show_book
    }

    return render(request, "books/show.html", context=context);


def book_search(booksList, id):
    for book in books:
        if int(book["id"]) == id:
            return book



#     return render(request, "books/index.html", context= context)
#
# def welcome(request, book_id):
#     context = {
#         "id": book_id
#     }
#     return render(request, "books/book.html", context=context)


