
from django.forms.models import modelform_factory
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from reviews.models import Review
from .forms import ReviewCreateForm, ReviewDeleteForm
from books.models import Book

# Create your views here.

def create_review(request: HttpRequest, book_slug: slug) -> HttpResponse:
    book = get_object_or_404(Book, slug=book_slug)
    form = ReviewCreateForm(request.POST or None)

    if form.is_valid():
        review = form.save(commit=False)
        review.book = book
        review.save()
        return redirect('book-detail', slug=book_slug)

    context = {
        'form': form,
        "book": book,
    }

    return render(request, 'reviews/create.html', context)

def edit_review(request: HttpRequest, pk: int) -> HttpResponse:
    review = get_object_or_404(Review, pk=pk)

    if request.user.is_staff:
        ReviewEditForm = modelform_factory(Review, fields="__all__")
    else:
        ReviewEditForm = modelform_factory(Review, exclude=['book'])

    form = ReviewEditForm(request.POST or None, instance=review)

    if form.is_valid():
        form.save()
        return redirect('book-detail', review.book.slug)

    context = {
        "form": form,
    }

    return render(request, 'reviews/edit.html', context)

def detail_review(request: HttpRequest, pk: int) -> HttpResponse:
    review = get_object_or_404(Review, pk=pk)

    context = {
        "review": review,
    }

    return render(request, 'reviews/detail.html', context)

def delete_review(request: HttpRequest, pk: int) -> HttpResponse:
    review = get_object_or_404(Review, pk=pk)
    form = ReviewDeleteForm(instance=review)

    if request.method == "POST":
        review.delete()
        return redirect('book-list')

    context = {
        "form": form,
    }

    return render(request, 'reviews/delete.html', context)
