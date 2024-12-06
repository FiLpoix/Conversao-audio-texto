from rest_framework import serializers
from .models import Conversao

class ConversaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conversao
        fields = ['id', 'texto', 'audio', 'data_criacao']
    
class TextToAudioSerializer(serializers.Serializer):
    text = serializers.CharField(max_length=500)
    language = serializers.ChoiceField(choices=[('en', 'English'), ('pt', 'Portuguese')], default='pt')