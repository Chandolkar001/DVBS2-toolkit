from django.urls import path, include
from .views import FileListCreateView, FileRetrieveView, file_process_view



urlpatterns = [
    path('files/', FileListCreateView.as_view(), name='file-list-create'),
    path('files/<int:pk>/', FileRetrieveView.as_view(), name='file-retrieve'),
    path('files/process/', file_process_view, name="file-process"),
]