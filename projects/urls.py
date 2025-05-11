from django.urls import path
from .views import project_get_view
urlpatterns = [
    path('projects/', project_get_view, name='project-list'),
]
