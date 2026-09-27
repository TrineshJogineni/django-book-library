from django.urls import path
from .views import book_library_view

urlpatterns = [
    path('', book_library_view, name='book_library'),
]