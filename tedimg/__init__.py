from flask import Flask
app = Flask(__name__)

app.config.update(
    SITE_NAME="TedImg",
    STORAGE_PATH="/tmp/images",
    WEB_PATH="/images",
)

import tedimg.views
