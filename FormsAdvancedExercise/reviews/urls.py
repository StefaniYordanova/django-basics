from django.urls import path, include
from . import views

urlpatterns = [
    path('create/', views.create_review, name='review-create'),
    path('<int:pk>/', include([
        path('detail/', views.detail_review, name='review-detail'),
        path('edit/', views.edit_review, name='review-edit'),
        path('delete/', views.delete_review, name='review-delete'),
    ]))
]