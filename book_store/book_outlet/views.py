from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.db.models import Avg, Min, Max

from .models import Book

# Create your views here.

def index(request):
  books = Book.objects.all().order_by('-rating')
  num_books = books.count()
  avg_rating = books.aggregate(Avg('rating'), Min('rating'), Max('rating'))
  return render(request, 'book_outlet/index.html', {
    "books": books,
    "total_number_of_books": num_books,
    "avg_rating": avg_rating['rating__avg'],
    "min_rating": avg_rating['rating__min'],
    "max_rating": avg_rating['rating__max']
  })
  

def book_detail(request, slug):
  # try:
  #   books = Book.objects.get(slug=slug)
  # except:
  #   raise Http404()
  book = get_object_or_404(Book, slug=slug)
  return render(request, 'book_outlet/book_detail.html', {
      "title": book.title,
      "author": book.author,
      "rating": book.rating,
      "is_bestSeller": book.is_bestSelling
  })
