from django.forms.models import modelform_factory
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from .forms import BookCreateForm, BookDeleteForm

# Create your views here.
def landing_page(request: HttpRequest) -> HttpResponse:
    latest_books = Book.objects.order_by('-updated_at', 'title')[:3]

    context = {
        "latest_books": latest_books,
    }

    return render(request, 'books/landing_page.html', context)

def books_list(request: HttpRequest) -> HttpResponse:
    books = Book.objects.order_by('-publishing_date', 'title')

    context = {
        "books": books,
    }

    return render(request, 'books/list.html', context)

def create_book(request: HttpRequest) -> HttpResponse:
    form = BookCreateForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('book-list')

    context = {
        "form": form,
    }

    return render(request, 'books/create.html', context)

def detail_book(request: HttpRequest, slug: slug) -> HttpResponse:
    book = get_object_or_404(Book, slug=slug)

    context = {
        "book": book,
    }

    return render(request, 'books/detail.html', context)

def edit_book(request: HttpRequest, slug: slug) -> HttpResponse:
    book = get_object_or_404(Book, slug=slug)

    if request.user.is_staff:
        BookEditForm = modelform_factory(Book, fields="__all__")
    else:
        BookEditForm = modelform_factory(Book, exclude=['slug', 'isbn'])

    form = BookEditForm(request.POST or None, instance=book)

    if form.is_valid():
        form.save()
        return redirect('book-list')

    context = {
        "form": form,
        "book": book,
    }

    return render(request, 'books/edit.html', context)

def delete_book(request: HttpRequest, slug: slug) -> HttpResponse:
    book = get_object_or_404(Book, slug=slug)
    form = BookDeleteForm(instance=book)

    if request.method == "POST":
        book.delete()
        return redirect('book-list')

    context = {
        "form": form,
        "book": book,
    }

    return render(request, 'books/delete.html', context)
