from tedimg import app, images

import flask
import os


@app.route('/')
def index():
    return flask.render_template("index.html")


@app.route('/show/<path:path>')
def show(path):
    root = flask.url_for("index", _external=True)
    image, thumb = images.get_image(root, path)
    return flask.render_template(
        "show.html",
        image=image, thumb=thumb,
        thumb_size=app.config["THUMB_SIZE"]
    )


@app.route('/upload', methods=['POST'])
def upload():
    uploaded = flask.request.files['file']
    url = flask.request.form['url']
    # Get an image object from the uploaded image or URL
    try:
        if uploaded:
            image = images.image_from_file(uploaded)
            filename = os.path.basename(uploaded.filename)
        elif url:
            image = images.image_from_file(uploaded)
            filename = os.path.basename(uploaded.filename)
        else:
            return flask.render_template("error.html", message="Missing image.")
    except Exception as error:
        raise
        return flask.render_template("error.html", message="Could not read your image.")
    # Save the image to a local file
    result = images.save_with_thumbnail(image, filename)
    return flask.redirect("/show/" + result)
