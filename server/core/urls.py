from django.urls import path, include
from .views import FileListCreateView, FileRetrieveView, file_process_view, get_extra_data_view, process_ts_pcap_view, get_analysis_report_view, process_gse



urlpatterns = [
    path('files/', FileListCreateView.as_view(), name='file-list-create'),
    path('files/<int:pk>/', FileRetrieveView.as_view(), name='file-retrieve'),
    path('files/process/', file_process_view, name="file-process"),
    path('files/extra_data/<int:id>/', get_extra_data_view, name="extra-data"),
    path('files/videostream/', process_ts_pcap_view, name="file-process-ts"),
    path('files/analysis/', get_analysis_report_view, name="file-analysis"),
    path('files/gse/', process_gse, name="file-gse"),


]