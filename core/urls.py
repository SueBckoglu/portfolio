from django.urls import path
from .views import index, contact_form
from . import views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', index, name='index'),
    path('index.html', contact_form, name='contact_form'),
    # Add other URL patterns for blog and portfolio if needed
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)