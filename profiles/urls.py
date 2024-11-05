# profiles/urls.py

from django.urls import path
from .views import register, login_view, home  # Import necessary views

urlpatterns = [
    path('register/', register, name='register'),  # Registration URL
    path('login/', login_view, name='login'),  # Login URL
    path('', home, name='home'),  # Home URL (optional if it exists)
]
