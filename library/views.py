from django.shortcuts import get_object_or_404, render
from django.views import generic

from .models import Book, Author


class IndexView(generic.ListView):
    template_name = 'library/index.html'
    context_object_name = 'total_book_list'

    def get_queryset(self):
        total_book_list = Book.objects.order_by('-has_been_read', 'title')
        return total_book_list

    def get_context_data(self, **kwargs):
        number_total_book_list = len(Book.objects.order_by('-has_been_read', 'title'))
        number_read_book_list = len(Book.objects.filter(has_been_read=True))

        context = super(IndexView, self).get_context_data(**kwargs)
        context['number_total_book_list'] = number_total_book_list
        context['number_read_book_list'] = number_read_book_list
        
        return context

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
    total_book_list = Book.objects.filter(author=author_id).order_by('-has_been_read', 'title')
    number_total_book_list = len(total_book_list)
    read_book_list = Book.objects.filter(author=author_id, has_been_read=True)
    number_read_book_list = len(read_book_list)

    return render(request, 'library/author_detail.html', {
            'author': author,
            'total_book_list': total_book_list,
            'number_total_book_list': number_total_book_list,
            'number_read_book_list': number_read_book_list
        }
    )
