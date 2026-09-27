from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Book
from .forms import BookForm

def book_library_view(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Book added successfully!")
            return redirect('book_library')
    else:
        form = BookForm()

    books = Book.objects.all().order_by('-created_at')
    return render(request, 'books/book_list.html', {'form': form, 'books': books, 'total_books': books.count()})