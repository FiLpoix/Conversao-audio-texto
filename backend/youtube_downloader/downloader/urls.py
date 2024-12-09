from django.urls import path
from .views import YouTubeVideoView

urlpatterns = [
    path('ytdownloader/', YouTubeVideoView.as_view(), name='youtube-video'),
]