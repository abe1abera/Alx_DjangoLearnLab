# urls.py (relationship_app)
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    # function-based view
    path("books/", views.list_books, name="list-books"),

    # class-based detail view
    path("library/<int:pk>/", views.LibraryDetailView.as_view(), name="library-detail"),

    # (auth routes are optional here if you already have them)
    path("login/", LoginView.as_view(template_name="relationship_app/login.html"), name="login"),
    path("logout/", LogoutView.as_view(template_name="relationship_app/logout.html"), name="logout"),
]
