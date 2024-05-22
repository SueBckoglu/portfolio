from django.urls import path
from .views import index, contact_form
from . import views


urlpatterns = [
    path('', index, name='index'),
    path('index.html', contact_form, name='contact_form'),
    # Add other URL patterns for blog and portfolio if needed
]