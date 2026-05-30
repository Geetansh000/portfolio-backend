from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response
from django.core.cache import cache
from .models import Project
from .serializers import (
    ProjectDetailSerializer,
    ProjectListSerializer,
    ProjectCreateSerializer,
)

class ProjectViewSet(viewsets.ModelViewSet):
    lookup_field = 'slug'
    list_cache_timeout = 60 * 5
    detail_cache_timeout = 60 * 15

    def get_queryset(self):
        if self.action == 'list':
            # Avoid loading large JSON fields for listing responses.
            return Project.objects.only(
                'id',
                'slug',
                'title',
                'short_description',
                'type',
                'color',
                'role',
                'icon',
            )

        return Project.objects.select_related('created_by', 'updated_by')

    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        elif self.request.method in ['POST', 'PUT', 'PATCH', 'DELETE']:
            return [IsAdminUser()]
        return []  # Default: disallow other methods

    def get_serializer_class(self):
        match self.action:
            case 'list':
                return ProjectListSerializer
            case 'create' | 'update' | 'partial_update':
                return ProjectCreateSerializer
            case _:
                return ProjectDetailSerializer

    def update(self, request, *args, **kwargs):
        kwargs['partial'] = True  # Allow partial updates via PUT
        return super().update(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        cache_key = 'projects:list'
        cached_data = cache.get(cache_key)
        if cached_data is not None:
            return Response(cached_data)

        response = super().list(request, *args, **kwargs)
        if response.status_code == 200:
            cache.set(cache_key, response.data, self.list_cache_timeout)
        return response

    def retrieve(self, request, *args, **kwargs):
        slug = kwargs.get(self.lookup_field)
        cache_key = f'projects:detail:{slug}'
        cached_data = cache.get(cache_key)
        if cached_data is not None:
            return Response(cached_data)

        response = super().retrieve(request, *args, **kwargs)
        if response.status_code == 200:
            cache.set(cache_key, response.data, self.detail_cache_timeout)
        return response

    def _invalidate_project_cache(self, slug=None):
        cache.delete('projects:list')
        if slug:
            cache.delete(f'projects:detail:{slug}')

    def perform_create(self, serializer):
        project = serializer.save()
        self._invalidate_project_cache(project.slug)

    def perform_update(self, serializer):
        old_slug = serializer.instance.slug
        project = serializer.save()
        self._invalidate_project_cache(old_slug)
        if project.slug != old_slug:
            self._invalidate_project_cache(project.slug)

    def perform_destroy(self, instance):
        slug = instance.slug
        instance.delete()
        self._invalidate_project_cache(slug)
