from tedimg import app, images

import flask
import urllib
import os


@app.route('/')
def index():
    return flask.render_template("index.html")


@app.route('/show/<path:path>')
def show(path):
    root = flask.url_for("index", _external=True)
    image, thumb = images.get_image(root, path)
    return flask.render_template("show.html", image=image, thumb=thumb)


@app.route('/upload', methods=['POST'])
def upload():
    url = flask.request.form.get('url')
    uploaded = flask.request.files.get('file')
    # Get an image object from the uploaded image or URL
    try:
        if uploaded:
            image = images.image_from_file(uploaded)
            filename = os.path.basename(uploaded.filename)
        elif url:
            image = images.image_from_url(url)
            parsed = urllib.parse.urlparse(url)
            filename = os.path.basename(parsed.path)
        else:
            return flask.render_template("error.html", message="Missing image.")
    except Exception as error:
        __import__("traceback").print_exc()
        return flask.render_template("error.html", message="Could not store your image.")
    # Save the image to a local file
    result = images.save_with_thumbnail(image, filename)
    return flask.redirect("/show/" + result)
