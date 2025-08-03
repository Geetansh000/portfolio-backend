from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView as TokeenObtainView,
)

urlpatterns = [
    path("login/", TokeenObtainView.as_view(), name="login"),
    
]
