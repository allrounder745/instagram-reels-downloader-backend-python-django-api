from django.urls import path
from .views import ReelDownloadAPI

urlpatterns = [
    path('api/download/', ReelDownloadAPI.as_view(), name='download_reel_api'),
]
