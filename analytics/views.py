from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Visitor
from django.utils.timezone import now


def get_client_ip(request):
    x_forwarded = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded:
        ip = x_forwarded.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


@api_view(['POST'])
def track_visit(request):
    ip = get_client_ip(request)
    visitor, created = Visitor.objects.get_or_create(ip_address=ip)
    if not created:
        visitor.visit_count += 1
        visitor.last_visited = now()
        visitor.save()
    return Response({"message": "Visit recorded"})


@api_view(['GET'])
def get_stats(request):
    total_views = sum(v.visit_count for v in Visitor.objects.all())
    unique_visitors = Visitor.objects.count()
    return Response({
        "total_views": total_views,
        "unique_visitors": unique_visitors,
    })
