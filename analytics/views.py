from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAdminUser
from .models import Visitor
from .serializers import VisitorSerializer
from rest_framework.response import Response
from rest_framework import status
from django.utils.timezone import now

# Create your views here.
class VisitorViewSet(viewsets.ModelViewSet):
    queryset = Visitor.objects.all()
    serializer_class = VisitorSerializer
    http_method_names = ['get', 'post', 'head']

    def get_permissions(self):
        if self.request.method == 'GET':
            return [IsAdminUser()]
        elif self.request.method == 'POST':
            return [AllowAny()]
        return []  # Default: disallow other methods

    def create(self, request, *args, **kwargs):
        ip = self.get_client_ip(request)
        visitor, created = Visitor.objects.get_or_create(ip_address=ip)
        if not created:
            visitor.visit_count += 1
            visitor.last_visited = now()
            visitor.save()
        serializer = self.get_serializer(visitor)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def get_client_ip(self, request):
        x_forwarded = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded:
            return x_forwarded.split(',')[0]
        return request.META.get('REMOTE_ADDR')