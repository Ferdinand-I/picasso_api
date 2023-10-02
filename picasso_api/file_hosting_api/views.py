from rest_framework.generics import ListAPIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from .models import FileModel
from .serializers import FileSerializer
from .tasks import change_processed_flag


class FileUploaderView(APIView):
    """Handles 'upload/' endpoint."""
    http_method_names = ['post', ]

    def post(self, request: Request):
        """POST-method."""
        serializer = FileSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
        validated_data = serializer.validated_data
        file_created = FileModel.objects.create(**validated_data)
        # Calling task asynchroniously after saving file on server
        change_processed_flag.delay(file_created)
        return Response(
            FileSerializer(file_created).data, status=HTTP_201_CREATED)


class FilesListView(ListAPIView):
    """Handles 'files/' endpoint."""
    queryset = FileModel.objects.all()
    serializer_class = FileSerializer
    http_method_names = ['get', ]
