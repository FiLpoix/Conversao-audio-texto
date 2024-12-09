from rest_framework import serializers
from .models import YouTubeVideo

class YouTubeVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = YouTubeVideo
        fields = ['id', 'url', 'title', 'format', 'created_at', 'updated_at']
