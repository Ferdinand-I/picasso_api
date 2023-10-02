from django.db import models

from .utils import get_upload_path_depends_on_extension


class FileModel(models.Model):
    """File model."""
    file = models.FileField(
        upload_to=get_upload_path_depends_on_extension, unique=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    processed = models.BooleanField(default=False)

    def __str__(self):
        return self.file.name
