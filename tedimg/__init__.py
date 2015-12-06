from flask import Flask
app = Flask(__name__)

app.config.update(
    SITE_NAME="TedImg",
    FULL_STORAGE="/tmp/images",
    THUMB_STORAGE="/tmp/images/thumb",
    FULL_WEB="image",
    THUMB_WEB="images/thumb",
    THUMB_SIZE=100
)

import tedimg.views
