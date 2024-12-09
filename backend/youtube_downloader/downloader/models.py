from django.db import models

# Create your models here.
from django.db import models

class YouTubeVideo(models.Model):
    url = models.URLField(max_length=500, verbose_name="URL do Vídeo")
    title = models.CharField(max_length=255, verbose_name="Título", blank=True, null=True)
    format = models.FileField(upload_to='videos/', choices=[
        ('mp4', 'MP4'),
        ('mp3', 'MP3'),
    ], default='mp4', verbose_name='formato do arquivo')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Data de Criação")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Última Atualização")

    def __str__(self):
        return f"{self.title or 'Vídeo Desconhecido'}"
