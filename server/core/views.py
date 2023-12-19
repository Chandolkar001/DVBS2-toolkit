# views.py
from rest_framework import generics
from .models import File
from .serializers import FileSerializer

class FileListCreateView(generics.ListCreateAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer

class FileRetrieveView(generics.RetrieveAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer
