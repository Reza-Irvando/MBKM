from app import app
from app.controllers import tes

app.route("/", methods = ["GET"])(tes.index)
app.route("/create", methods = ["POST"])(tes.create)