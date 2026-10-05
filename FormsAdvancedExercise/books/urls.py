from django.urls import path, include
from . import views


urlpatterns = [
    path('list/', views.books_list, name='book-list'),
    path('create/', views.create_book, name='book-create'),
    path('<slug:slug>/', include([
        path('detail/', views.detail_book, name='book-detail'),
        path('edit/', views.edit_book, name='book-edit'),
        path('delete/', views.delete_book, name='book-delete'),
    ])),
]