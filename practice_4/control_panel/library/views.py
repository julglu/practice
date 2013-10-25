# Create your views here.
from django.shortcuts import render
from django.db.models import Count
from library.models import Book
from library.models import Author
book_authors={}
context={}


def author_list(request):
    all_authors=Author.objects.all()
    context['author_list']=all_authors
    return render(request, 'authors.html', context)


def book_list(request):
    all_books=Book.objects.all()
    context['book_list']=all_books
    return render(request, 'books.html', context)


def author_card(request, author_id):
    author_n=Author.objects.get(pk=author_id)
    context['author_n']=author_n
    return render(request, 'author_card.html', context)


def book_card(request, book_id):
    book_n=Book.objects.get(pk=book_id)
    context['book_n']=book_n
    return render(request, 'book_card.html', context)
