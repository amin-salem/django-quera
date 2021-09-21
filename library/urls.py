from django.urls import path
from django.urls.resolvers import URLPattern
from .views import book_detail

URLPattern = [
    path('books/<int:book_id>/', book_detail, name = book_detail),
]