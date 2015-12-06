from tedimg import app
from flask import send_from_directory

app.config.update(
    SITE_NAME="TeDomum Images",
    FULL_STORAGE="./tedimg/static/images",
    THUMB_STORAGE="./tedimg/static/images/thumb",
    FULL_WEB="static/images",
    THUMB_WEB="static/images/thumb"
)

app.run(debug=True)
