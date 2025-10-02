from django.urls import path, include
from rest_framework import routers
from .views import AuthorViewSet, BookViewSet

router = routers.DefaultRouter()
router.register(r'authors', AuthorViewSet)
router.register(r'books', BookViewSet)

urlpatterns = [
    path('', include(router.urls)),
]



# api/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.ListView.as_view(), name='book-list'),
    path('books/create/', views.CreateView.as_view(), name='book-create'),
    path('books/<int:pk>/', views.DetailView.as_view(), name='book-detail'),
    path('books/<int:pk>/update/', views.UpdateView.as_view(), name='book-update'),
    path('books/<int:pk>/delete/', views.DeleteView.as_view(), name='book-delete'),
]
