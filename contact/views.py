from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Contact
from .serializers import ContactSerializer
import json

# View to handle POST request (creating a new contact)
@csrf_exempt
def contact_post_view(request):
    if request.method == 'POST':
        try:
            # Parse JSON body from the request
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)

        # Validate and save data using ContactSerializer
        serializer = ContactSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    return JsonResponse({"error": "Method not allowed"}, status=405)


# View to handle GET request (retrieving all contacts)
def contact_get_view(request):
    if request.method == 'GET':
        contacts = Contact.objects.all()
        serializer = ContactSerializer(contacts, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    return JsonResponse({"error": "Method not allowed"}, status=405)
