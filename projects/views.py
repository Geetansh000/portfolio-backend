from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import Project
from .serializers import ProjectSerializer
import json
from django.http import JsonResponse

def createSlug(title):
    import re
    title = title.lower()
    slug = re.sub(r'\W+', '_', title)
    slug = re.sub(r'_+', '_', slug).strip('_')
    return slug
# Create your views here.
def createProject(request):
    try:
        # Parse JSON body from the request
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)

    data['slug'] = createSlug(data['title'])
    # Validate and save data using ContactSerializer
    serializer = ProjectSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def project_get_view(request):
    if request.method == 'GET':
        projects = Project.objects.values(
            'id',
            'slug',
            'title',
            'short_description',
            'type',
            'color',
            'role',
            'icon',
            'created_at',
        )
        if projects.count() == 0:
            return JsonResponse({'error': 'No projects found'}, status=404)
        serializer = ProjectSerializer(projects, many=True)
        return JsonResponse(serializer.data, safe=False)
    if request.method == 'POST':
        return createProject(request)

    return JsonResponse({'error': 'Method not allowed'}, status=405)

def project_get_detail_view(request, slug):
    if request.method == 'GET':
        project = Project.objects.get(slug=slug)
        serializer = ProjectSerializer(project)
        return JsonResponse(serializer.data, safe=False)
    return JsonResponse({'error': 'Method not allowed'}, status=405)