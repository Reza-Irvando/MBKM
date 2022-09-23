from app import app
from app.controllers import user_management

app.route("/register", methods = ["POST"])(user_management.Register)
app.route("/login", methods = ["POST"])(user_management.Login)