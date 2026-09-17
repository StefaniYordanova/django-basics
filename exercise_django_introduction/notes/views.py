from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from .models import Note

# Create your views here.

def index(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Hello, world!")

def index1(request: HttpRequest):
    context = {
        'notes': Note.objects.all(),
    }

    return render(request, 'index1.html', context)
