# contact/urls.py

from django.urls import path
from contact_app.views import contact_form  # Import the contact view function

urlpatterns = [
    path('contact_form/', contact_form, name='k'),
]
