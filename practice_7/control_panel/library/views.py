# Create your views here.
from library.models import Book
from library.models import Author
from django.views.generic import ListView
from django.views.generic import DetailView


class BooksList(ListView):
    model = Book
    context_object_name = 'books'
    template_name = "book_list.html"


class BookDetail(DetailView):
    model = Book
    queryset = Book.objects.all()
    template_name = "book_detail.html"


class AuthorsList(ListView):
    model = Author
    context_object_name = 'authors'
    template_name = "author_list.html"


class AuthorDetail(DetailView):
    model = Author
    queryset = Author.objects.all()
    template_name = "author_detail.html"
