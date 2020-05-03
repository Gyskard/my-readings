from django.urls import path

from . import views

app_name = 'library'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('book/', views.BookListView.as_view(), name='book_list'),
    path('book/<int:pk>/', views.BookDetailView.as_view(), name='book_detail'),
    path('author/', views.AuthorListView.as_view(), name='author_list'),
    path('author/<int:author_id>/', views.AuthorDetailView, name='author_detail'),
]