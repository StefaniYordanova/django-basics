from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.
def landing_page(request: HttpRequest) -> HttpResponse:
    return render(request, 'books/landing_page.html')

def books_list(request: HttpRequest) -> HttpResponse:
    return render(request, 'books/list.html')

def create_book(request: HttpRequest) -> HttpResponse:
    return render(request, 'books/create.html')

def detail_book(request: HttpRequest, slug: slug) -> HttpResponse:
    return render(request, 'books/detail.html')

def edit_book(request: HttpRequest, slug: slug) -> HttpResponse:
    return render(request, 'books/edit.html')

def delete_book(request: HttpRequest, slug: slug) -> HttpResponse:
    return render(request, 'books/delete.html')
