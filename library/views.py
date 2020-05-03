from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Book, Author

class IndexView(generic.ListView):
    template_name = 'library/index.html'
    context_object_name = 'latest_book_list'

    def get_queryset(self):
        return Book.objects.all()[:10]

class BookListView(generic.ListView):
    template_name = 'library/book_list.html'
    context_object_name = 'book_list'

    def get_queryset(self):
        return Book.objects.all()

class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'library/book_detail.html'

class AuthorListView(generic.ListView):
    template_name = 'library/author_list.html'
    context_object_name = 'author_list'

    def get_queryset(self):
        return Author.objects.all()

def AuthorDetailView(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    book_list = Book.objects.filter(author=author_id)
    return render(request, 'library/author_detail.html', {'author': author, 'book_list': book_list})