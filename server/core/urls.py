from django.urls import path, include
from .views import FileListCreateView, FileRetrieveView


urlpatterns = [
    path('files/', FileListCreateView.as_view(), name='file-list-create'),
    path('files/<int:pk>/', FileRetrieveView.as_view(), name='file-retrieve'),
]