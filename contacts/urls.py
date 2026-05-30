from django.urls import path, include
from .views import ContactViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('', ContactViewSet, basename='')

urlpatterns = [
    path('', include(router.urls)),
]   