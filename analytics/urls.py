from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import VisitorViewSet

router = SimpleRouter()
router.register('', VisitorViewSet, basename='')
urlpatterns = [path('', include(router.urls))]
