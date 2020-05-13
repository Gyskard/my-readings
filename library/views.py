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
        context = super(IndexView, self).get_context_data(**kwargs)
        context['number_total_book_list'] = len(Book.objects.order_by())
        context['number_read_book_list'] = len(Book.objects.filter(has_been_read=True))
        context['number_author'] = len(Author.objects.order_by())
        return context

class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'library/book_detail.html'

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

class SearchView(generic.ListView):
    template_name = 'library/search.html'
    context_object_name = 'data'

    def get_queryset(self):
        number_all_book = Count('book')
        number_read_book = Count('book', filter=Q(book__has_been_read=True))
        context = {
            'books': Book.objects.all().order_by('title'),
            'authors': Author.objects.all().annotate(number_all_book=number_all_book).annotate(number_read_book=number_read_book).order_by('name')
        }
        return context