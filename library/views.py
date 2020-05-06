from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.db.models import Count, Q

from .models import Book, Author


class IndexView(generic.ListView):
    template_name = 'library/index.html'
    context_object_name = 'total_book_list'

    def get_queryset(self):
        total_book_list = Book.objects.order_by('id')[:10]
        return total_book_list

    def get_context_data(self, **kwargs):
        number_total_book_list = len(Book.objects.order_by())
        number_read_book_list = len(Book.objects.filter(has_been_read=True))
        context = super(IndexView, self).get_context_data(**kwargs)
        context['number_total_book_list'] = number_total_book_list
        context['number_read_book_list'] = number_read_book_list
        return context

class BookListView(generic.ListView):
    template_name = 'library/book_list.html'
    context_object_name = 'book_list'

    def get_queryset(self):
        return Book.objects.all().order_by('title')

    def get_context_data(self, **kwargs):
        number_total_book = len(Book.objects.order_by())
        number_read_book = len(Book.objects.filter(has_been_read=True))
        context = super(BookListView, self).get_context_data(**kwargs)
        context['number_total_book'] = number_total_book
        context['number_read_book'] = number_read_book
        return context


class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'library/book_detail.html'


class AuthorListView(generic.ListView):
    template_name = 'library/author_list.html'
    context_object_name = 'author_list'

    def get_queryset(self):
        #.annotate(number_total_book=Count('book__id'))
        number_all_book = Count('book')
        number_read_book = Count('book', filter=Q(book__has_been_read=True))
        return Author.objects.all().annotate(number_all_book=number_all_book).annotate(number_read_book=number_read_book).order_by('name')

    def get_context_data(self, **kwargs):
        number_total_author = len(Author.objects.order_by())
        context = super(AuthorListView, self).get_context_data(**kwargs)
        context['number_total_author'] = number_total_author
        return context

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
