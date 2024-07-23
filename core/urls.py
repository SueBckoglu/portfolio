from django.urls import path
from .views import index, contact_form

urlpatterns = [
    path('', index, name='index'),  # Homepage
    path('contact/', contact_form, name='contact_form'),  # Contact form
    # Add other URL patterns for blog and portfolio if needed
]
