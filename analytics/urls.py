from django.urls import path
from .views import track_visit,get_stats
urlpatterns = [
    path('add/', track_visit, name='track-visit'),
    path('stats/', get_stats, name='get-stats'),
]
