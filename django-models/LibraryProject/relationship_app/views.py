from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views.generic.detail import DetailView
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView

from .models import Book, Library

# ----------------------
# Function-based view
# ----------------------
def list_books(request):
    books = Book.objects.all()
    return render(request, "r
