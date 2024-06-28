# Import the admin module from django.contrib
from django.contrib import admin

# Import the path and include functions from django.urls
from django.urls import path, include

# Define the URL patterns for the project
urlpatterns = [
    # Include the URL patterns from the pages application
    path('', include('pages.urls')),

    # URL pattern for the Django admin site
    path('admin/', admin.site.urls),
]
