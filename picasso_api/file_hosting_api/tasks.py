from celery import shared_task


@shared_task
def change_processed_flag(instance):
    """Asynchronious task that emulate file processing after uploading."""
    from .models import FileModel
    # in case of something goes wrong in a view
    if not isinstance(instance, FileModel):
        return f'Processing of "{instance}" cannot be finished!'
    instance.processed = True
    instance.save()
    return f'Processing of "{instance.file}" successfully finished!'
