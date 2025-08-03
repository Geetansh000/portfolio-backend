from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def home(request):
    print("Home view accessed")
    return Response("Welcome to the API")
