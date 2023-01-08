from app import app
from app.controllers import content

app.route("/content/create",   methods=["POST"])(content.ContentCreate)
app.route("/content/list",   methods=["GET"])(content.ContentList)