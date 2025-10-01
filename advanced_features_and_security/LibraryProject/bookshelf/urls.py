from django.urls import path
from .views import example_form_view

urlpatterns = [
    path("example-form/", example_form_view, name="example-form"),
]

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bookshelf/', include('bookshelf.urls')),  # add this if not present
]
