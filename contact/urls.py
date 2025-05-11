from django.urls import path
from .views import contact_get_view, contact_post_view
from .serializers import ContactSerializer

urlpatterns = [
    path('contacts/', contact_get_view, name='contact-list'),  # GET request
    path('contacts/create/', contact_post_view, name='contact-create'),  # POST request
]