from tedimg import app
from flask import send_from_directory

app.config.update(
    STORAGE_PATH="./tedimg/static/images",
    WEB_PATH="/static/images"
)

app.run(debug=True)
