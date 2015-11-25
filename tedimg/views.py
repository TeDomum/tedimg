from tedimg import app, images

import flask


@app.route('/')
def index():
    return flask.render_template("index.html")


@app.route('/show/<path:path>')
def show(path):
    image = images.get_image(path)
    return flask.render_template("show.html", image=image)
