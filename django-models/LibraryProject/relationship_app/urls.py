from django.urls import path
from .views import (
    list_books,
    LibraryDetailView,
    register,
    CustomLoginView,
    CustomLogoutView,
)

urlpatterns = [
    # Book and Library views
    path("books/", list_books, name="list-books"),
    path("library/<int:pk>/", LibraryDetailView.as_view(), name="library-detail"),

    # Authentication views
    path("register/", register, name="register"),
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", CustomLogoutView.as_view(), name="logout"),
]
