from tedimg import app

from os import path


def get_image(name):
    """ Try and get basic image attributes.
    """
    filename = path.basename(name)
    return path.join(app.config["WEB_PATH"], filename)
