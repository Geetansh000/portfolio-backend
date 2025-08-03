
from .views import ProjectViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('', ProjectViewSet, basename='project')
urlpatterns = router.urls