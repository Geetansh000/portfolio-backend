from django.urls import path, include

urlpatterns = [
    path("user/", include("user.urls")),
    path("contacts/", include("contacts.urls")),
    path("projects/", include("projects.urls")),
    path('visitor/', include('analytics.urls')),
]