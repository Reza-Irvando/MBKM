from app import app
from app.controllers import user_management

# app.route("/register", methods = ["POST"])(user_management.Register)
# app.route("/login", methods = ["POST"])(user_management.Login)
# app.route("/listUser", methods = ["GET"])(user_management.ListUser)
# app.route("/updateUser/<userId>", methods = ["PUT"])(user_management.UpdateUser)
# app.route("/deleteUser", methods = ["POST"])(user_management.DeleteUser)

app.route ("/addList", methods = ["POST"])(user_management.AddList)
app.route ("/viewList", methods = ["GET"])(user_management.ViewList)
app.route ("/updateList", methods = ["PUT"])(user_management.UpdateList)
app.route ("/deleteList", methods = ["DELETE"])(user_management.DeleteList)
app.route ("/detailList", methods = ["GET"])(user_management.DetailList)