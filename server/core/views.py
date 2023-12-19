# views.py
from rest_framework import generics
from .models import File
from .serializers import FileSerializer
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .utils import process_pcap

class FileListCreateView(generics.ListCreateAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer

class FileRetrieveView(generics.RetrieveAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer

@csrf_exempt
def file_process_view(request):
    if request.method == 'POST' and request.FILES.get('file'):
        uploaded_file = request.FILES['file']
        file_name = uploaded_file.name
        file_type = request.POST.get("file_type")

        file = File(file = uploaded_file)
        file.save()
        result = process_pcap(file)

        return JsonResponse(result)
    res = HttpResponse(f"GET Request Not Allowed.")
    res.status_code = 400
    return res
