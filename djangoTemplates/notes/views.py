from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from .models import Note

# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    context = {
        'notes': Note.objects.all(),
    }

    return render(request, 'notes/index.html', context)