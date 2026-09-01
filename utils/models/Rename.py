import os
import uuid
from django.utils.deconstruct import deconstructible

@deconstructible
class PictureRename:
    def __init__(self, sub_path):
        self.path = sub_path

    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]
        new_filename = f'{uuid.uuid4().hex}.{ext}'

        return os.path.join(self.path, new_filename)