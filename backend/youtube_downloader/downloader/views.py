from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from pytube import YouTube
from .serializers import YouTubeVideoSerializer
import os


class YouTubeVideoView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = YouTubeVideoSerializer(data=request.data)

        if serializer.is_valid():
            url = serializer.validated_data['url']
            file_format = serializer.validated_data['format']

            try:
                yt = YouTube(url)
                # Escolher formato

                if file_format == 'mp4':
                    stream = yt.streams.filter(file_extension='mp4', progressive=True).first()
                else: 
                    stream = yt.streams.filter(only_audio=True, file_extension='mp4').first()
                # Realizar o download
                
                download_path = os.path.join(os.getcwd(), 'downloads')
                os.makedirs(download_path, exist_ok=True)
                file_path = stream.download(output_path=download_path)

                # Resposta de sucesso

                return Response(
                    {
                        'message': 'Vídeo baixado com sucesso!',
                        'file_path': file_path
                    },
                    status=status.HTTP_201_CREATED
                )
            
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

