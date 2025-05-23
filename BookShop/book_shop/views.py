from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from .forms import BookForm


def index(request):
    books = Book.objects.all()
    return render(request, 'index.html', context={'books': books})


def add_books(request):
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save(commit=False)
            book.save()
            return redirect('index')
    else:
        form = BookForm()

    books = Book.objects.all()
    return render(request, 'add_books.html', {'form': form, 'books': books})


def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'book_detail.html', {'book': book})
# Create your views here.
