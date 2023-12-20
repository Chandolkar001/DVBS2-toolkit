# views.py
from rest_framework import generics
from .models import File
from .serializers import FileSerializer
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .utils import process_pcap, get_extra_data, new_extra_data, process_ts_pcap, PID_analysis, multiple_video_extract
from .sohel import getGSE

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


@csrf_exempt
def get_extra_data_view(request,id):
        # try:
            file = File.objects.all().last()
            result = new_extra_data(file, int(id))
            return JsonResponse(result, safe=False)
        # except Exception as e:
        #     print(e)
        #     res = HttpResponse(f"File not found.")
        #     res.status_code = 404
        #     return res
    # res = HttpResponse(f"GET Request Not Allowed...")


@csrf_exempt
def process_ts_pcap_view(request):
    if request.method == 'POST' and request.FILES.get('file'):
        uploaded_file = request.FILES['file']

        file = File(file = uploaded_file)
        file.save()
        # result = process_ts_pcap(file)
        result = multiple_video_extract(file)

        return JsonResponse(result)
    res = HttpResponse(f"GET Request Not Allowed.")
    res.status_code = 400
    return res

@csrf_exempt
def get_analysis_report_view(request):
        # try:
            file = File.objects.all().last()
            result = PID_analysis(file)
            return JsonResponse(result)
        
@csrf_exempt
def process_gse(request):
    if request.method == 'POST' and request.FILES.get('file'):
        uploaded_file = request.FILES['file']

        file = File(file = uploaded_file)
        file.save()
        # result = process_ts_pcap(file)
        result = getGSE(file)

        return JsonResponse(result)
    res = HttpResponse(f"GET Request Not Allowed.")
    res.status_code = 400
    return res