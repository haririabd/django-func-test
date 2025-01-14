import os
from django.conf import settings

def upload_file(file):
    """
    Uploads a file to the specified directory and returns the file path.

    Args:
        file: The uploaded file object.

    Returns:
        The full path to the saved file.
    """
    file_path = os.path.join(settings.MEDIA_ROOT, 'csv_files', file.name)
    with open(file_path, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)
    return file_path