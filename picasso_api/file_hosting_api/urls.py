from django.urls import path

from .views import FileUploaderView, FilesListView

urlpatterns = [
    path('upload/', FileUploaderView.as_view(), name='upload'),
    path('files/', FilesListView.as_view(), name='files')
]
