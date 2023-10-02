import magic


def get_upload_path_depends_on_extension(instance, filename):
    """Little util to sort uploaded files with directories."""
    file = instance.file.read(2048)
    type_ = magic.from_buffer(file, mime=True)
    extension = type_.split('/')[-1]
    return f'{extension}/{filename}'
