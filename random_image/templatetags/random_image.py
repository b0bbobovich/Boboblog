import os
import random
from django import template
from django.conf import settings
from pathlib import Path

register = template.Library()

@register.simple_tag
def random_image(image_dir):
    try:
        valid_extensions = settings.RANDOM_IMAGE_EXTENSIONS
    except AttributeError:
        valid_extensions = ['.jpg','.jpeg','.png','.gif',]

    if image_dir:
        rand_dir = Path(settings.RANDOM_IMAGE_DIR) / image_dir

    else:
        rand_dir = Path(settings.STATIC_ROOT) / image_dir

    files = [f for f in os.listdir(rand_dir) if os.path.splitext(f)[1] in valid_extensions]

    result = Path(rand_dir) / random.choice(files)
    print(result)
    return result




