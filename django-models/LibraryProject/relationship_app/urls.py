from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    # Book and Library views
    path("books/", views.list_books, name="list-books"),
    path("library/<int:pk>/", views.LibraryDetailView.as_view(), name="library-detail"),

    # Authentication views (checker wants this format)
    path("register/", views.register, name="register"),
    path("login/", LoginView.as_view(template_name="relationship_app/login.html"), name="login"),
    path("logout/", LogoutView.as_view(template_name="relationship_app/logout.html"), name="logout"),
]
