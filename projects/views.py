from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAdminUser
from .models import Project
from .serializers import (
    ProjectDetailSerializer,
    ProjectListSerializer,
    ProjectCreateSerializer,
)

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    lookup_field = 'slug'

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
