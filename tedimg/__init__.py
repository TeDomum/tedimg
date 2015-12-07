from flask import Flask

import os

app = Flask(__name__)
app.debug = "FLASK_DEBUG" in os.environ

app.config.update(
    SITE_NAME=os.environ.get("SITE_NAME", "TedImg"),
    SOURCE_URL="https://git.tedomum.net/kaiyou/tedimg",
    HELP_URL="https://git.tedomum.net/kaiyou/tedimg",
    FULL_STORAGE=os.environ.get("FULL_STORAGE", "/data"),
    THUMB_STORAGE=os.environ.get("THUMB_STORAGE", "/data/thumb"),
    FULL_WEB=os.environ.get("FULL_WEB", "images"),
    THUMB_WEB=os.environ.get("THUMB_WEB", "images/thumb"),
    THUMB_SIZE=100
)

if (app.debug):
    from werkzeug import debug
    app.wsgi_app = debug.DebuggedApplication(app.wsgi_app, True)

import tedimg.views
