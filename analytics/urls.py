from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VisitorViewSet

router = DefaultRouter()
router.register('', VisitorViewSet, basename='')
urlpatterns = [path('', include(router.urls))]
