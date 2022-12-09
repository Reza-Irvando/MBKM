from app import app
from app.controllers import management

app.route("/auth/login",            methods=["POST"])   (management.Login)
app.route("/auth/register",         methods=["POST"])   (management.Register)
app.route("/auth/token/refresh",    methods=["GET"])   (management.RefreshToken)
app.route("/auth/logout",           methods=["DELETE"]) (management.Logout)
app.route("/user/profile",          methods=["GET"])    (management.Profile)

app.route("/management/unit/register", methods=["POST"])   (management.UnitRegister)
app.route("/management/user/register", methods=["POST"])   (management.UserRegister)