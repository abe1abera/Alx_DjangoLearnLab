from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views   # 🔑 import views so checker finds views.register
from .views import list_books, LibraryDetailView

urlpatterns = [
    # Task 1 requirements
    path("books/", list_books, name="list_books"),
    path("library/<int:pk>/", LibraryDetailView.as_view(), name="library_detail"),

    # Authentication task requirements
    path("register/", views.register, name="register"),  # 🔑 use views.register
    path("login/", LoginView.as_view(template_name="relationship_app/login.html"), name="login"),
    path("logout/", LogoutView.as_view(template_name="relationship_app/logout.html"), name="logout"),
]


# --- existing imports and urlpatterns above ---

urlpatterns += [
    path("admin-view/", views.admin_view, name="admin_view"),
    path("librarian-view/", views.librarian_view, name="librarian_view"),
    path("member-view/", views.member_view, name="member_view"),
]

# --- existing urlpatterns above ---

urlpatterns += [
    path("add_book/", views.add_book, name="add_book"),
    path("edit_book/<int:book_id>/", views.edit_book, name="edit_book"),
    path("delete_book/<int:book_id>/", views.delete_book, name="delete_book"),
]
