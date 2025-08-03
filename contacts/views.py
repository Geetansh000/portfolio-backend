from rest_framework import viewsets
from .models import Contact
from .serializers import ContactSerializer
from rest_framework.permissions import AllowAny, IsAdminUser
# Create your views here.
class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    def get_permissions(self):
        # Override to allow any user to access the viewset
        if self.request.method in ['POST']:
            return [AllowAny()]
        return [IsAdminUser()]