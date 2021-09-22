from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponse
from .models import Book
# Create your views here.

def book_detail(request, book_id):
    try:
        book = Book.objects.get(pk = book_id)
        context = {'book': book}
        return render(request, 'book_detail.html', context = context)
    except Book.DoesNotExist:
        return HttpResponse('<h2> Book matching query does not exist. </h2>')