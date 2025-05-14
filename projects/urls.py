from django.urls import path
from .views import project_get_view, project_get_detail_view

urlpatterns = [
    path('projects/', project_get_view, name='project-list'),
    path('projects/<slug:slug>', project_get_detail_view, name='project-detail'),
]
