
from .views import ProjectViewSet
from rest_framework.routers import SimpleRouter


router = SimpleRouter()
router.register('', ProjectViewSet, basename='project')
urlpatterns = router.urls
