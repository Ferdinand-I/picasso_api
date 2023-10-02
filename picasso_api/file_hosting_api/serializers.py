from rest_framework import serializers

from .models import FileModel


class FileSerializer(serializers.ModelSerializer):
    """File serializer."""
    file = serializers.FileField(required=True)
    uploaded_at = serializers.DateTimeField(read_only=True)
    processed = serializers.BooleanField(read_only=True)

    class Meta:
        model = FileModel
        exclude = ['id']
