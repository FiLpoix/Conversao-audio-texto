from django.db import models

# Create your models here.
class Conversao(models.Model):
    texto = models.TextField()
    audio = models.FileField(upload_to='audios/', null=True)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Conversão {self.id}'
