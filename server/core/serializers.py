from rest_framework import serializers
from .models import File

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ('file', 'file_type')
        extra_kwargs = {
            'file_type': {'required': False},
        }
        