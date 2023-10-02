from celery import shared_task


@shared_task
def change_processed_flag(instance):
    """Asynchronious task that emulate file processing after uploading."""
    instance.processed = True
    instance.save()
    return f'Processing of "{instance.file}" successfully finished!'
