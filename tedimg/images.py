from tedimg import app
from PIL import Image, ImageSequence

import os
import binascii
import requests
import io
import urllib


def get_image(root, name):
    """ Try and get basic image attributes.
    """
    filename = urllib.parse.quote(os.path.basename(name))
    return (root + os.path.join(app.config["FULL_WEB"], filename),
            root + os.path.join(app.config["THUMB_WEB"], filename))


def image_from_file(file_storage):
    """ Try and read the uploaded file.
    """
    image = Image.open(file_storage)
    return image


def image_from_url(url):
    """ Try and download an image from the given url.
    """
    response = requests.get(url)
    image = Image.open(io.BytesIO(response.content))
    return image


def save_with_thumbnail(image, filename):
    dest = "."
    while os.path.exists(os.path.join(app.config["FULL_STORAGE"], dest)):
        filename, _ = os.path.splitext(filename)
        ext = image.format.lower()
        random = binascii.hexlify(os.urandom(3)).decode('utf8')
        dest = "%s-%s.%s" % (filename, random, ext)
    # Grab some configuration
    full_file = os.path.join(app.config["FULL_STORAGE"], dest)
    thumb_file = os.path.join(app.config["THUMB_STORAGE"], dest)
    thumb_size = app.config["THUMB_SIZE"]
    # Save the image and thumbnail
    if image.format == 'GIF':
        image.save(full_file, format=image.format, save_all=True)
    else:
        image.save(full_file, format=image.format)
    image.thumbnail((thumb_size, thumb_size))
    image.save(thumb_file, format=image.format)
    return dest
