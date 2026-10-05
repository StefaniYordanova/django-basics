from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.

def create_review(request: HttpRequest) -> HttpResponse:
    return render(request, 'reviews/create.html')

def edit_review(request: HttpRequest, pk: int) -> HttpResponse:
    return render(request, 'reviews/edit.html')

def detail_review(request: HttpRequest, pk: int) -> HttpResponse:
    return render(request, 'reviews/detail.html')

def delete_review(request: HttpRequest, pk: int) -> HttpResponse:
    return render(request, 'reviews/delete.html')
