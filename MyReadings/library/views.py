from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.db.models import Count, Q

from .models import Book, Author


class IndexView(generic.ListView):
    template_name = 'library/index.html'
    context_object_name = 'total_book_list'

    def get_queryset(self):
        book_list = Book.objects.order_by('id')[:10]
        return book_list

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        authors = Author.objects.order_by()
        total_books = Book.objects.order_by()
        read_books = total_books.filter(has_been_read=True)
        context['number_author'] = len(authors)
        context['number_total_book_list'] = len(total_books)
        context['number_read_book_list'] = len(read_books)
        return context


class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'library/book_detail.html'


def AuthorDetailView(request, author_id):
    books = Book.objects.filter(author=author_id)
    total_book_list = books.order_by('-has_been_read', 'title')
    read_book_list = books.filter(has_been_read=True)
    return render(request, 'library/author_detail.html', {
            'author': get_object_or_404(Author, pk=author_id),
            'number_read_book_list': len(read_book_list),
            'number_total_book_list': len(total_book_list),
            'total_book_list': total_book_list,
        }
    )


class SearchView(generic.ListView):
    template_name = 'library/search.html'
    context_object_name = 'data'

    def get_queryset(self):
        context = {
            'books': Book.objects.all().order_by('title'),
            'authors': Author.objects.all()
            .annotate(number_all_book=Count('book'))
            .annotate(number_read_book=Count(
                'book',
                filter=Q(book__has_been_read=True)))
            .order_by('name')
        }
        return context
