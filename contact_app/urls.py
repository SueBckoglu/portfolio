from django.urls import path
from . import views

urlpatterns = [
    path('contact/', views.contact_view, name='contact'),
    # Add more URL patterns as needed
]
