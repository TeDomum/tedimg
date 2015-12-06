from tedimg import app
from PIL import Image

import os
import binascii


def get_image(root, name):
    """ Try and get basic image attributes.
    """
    filename = os.path.basename(name)
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


def save_with_thumbnail(image, filename):
    dest = "."
    while os.path.exists(os.path.join(app.config["FULL_STORAGE"], dest)):
        filename, ext = os.path.splitext(filename)
        random = binascii.hexlify(os.urandom(3)).decode('utf8')
        dest = "%s-%s%s" % (filename, random, ext)
    image.save(os.path.join(app.config["FULL_STORAGE"], dest))
    thumb_size = app.config["THUMB_SIZE"]
    image.thumbnail((thumb_size, thumb_size))
    image.save(os.path.join(app.config["THUMB_STORAGE"], dest))
    return dest
