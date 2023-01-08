from app import app
from app.controllers import management

app.route("/auth/login",            methods=["POST"])   (management.Login)
app.route("/auth/register",         methods=["POST"])   (management.Register)
app.route("/auth/token/refresh",    methods=["GET"])   (management.RefreshToken)
app.route("/auth/logout",           methods=["DELETE"]) (management.Logout)
app.route("/user/profile",          methods=["GET"])    (management.Profile)

app.route("/management/unit/register", methods=["POST"])   (management.UnitRegister)
app.route("/management/user/register", methods=["POST"])   (management.UserRegister)

app.route("/manajemen/account/login", methods=["POST"])   (management.accountLogin)
app.route("/manajemen/account/registerCorp", methods=["POST"])   (management.accountRegisterCORP)
app.route("/manajemen/account/registerCorpDb", methods=["POST"])   (management.accountRegisterDB)
app.route("/manajemen/account/registerSmb", methods=["POST"])   (management.accountRegisterSmb)

app.route("/manajemen/session/generate", methods=["GET"])   (management.sessionGenerateAccessToken)

app.route("/manajemen/access/findAll", methods=["GET"])  (management.accessFindAll)
app.route("/manajemen/access/findOne", methods=["GET"])  (management.accessFindOne)
app.route("/manajemen/access/insertOne", methods=["POST"])  (management.accessInsertOne)
app.route("/manajemen/access/updateOne", methods=["PUT"])  (management.accessUpdateOne)
app.route("/manajemen/access/deleteOne", methods=["DELETE"])  (management.accessDeleteOne)

app.route("/manajemen/permission/findAll", methods=["GET"])  (management.permissionFindAll)
app.route("/manajemen/permission/findOne", methods=["GET"])  (management.permissionFindOne)
app.route("/manajemen/permission/insertOne", methods=["POST"])  (management.permissionInsertOne)
app.route("/manajemen/permission/updateOne", methods=["PUT"])  (management.permissionUpdateOne)
app.route("/manajemen/permission/deleteOne", methods=["DELETE"])  (management.permissionDeleteOne)

app.route("/manajemen/role/findAll", methods=["GET"])  (management.roleFindAll)
app.route("/manajemen/role/findOne", methods=["GET"])  (management.roleFindOne)
app.route("/manajemen/role/insertOne", methods=["POST"])  (management.roleInsertOne)
app.route("/manajemen/role/updateOne", methods=["PUT"])  (management.roleUpdateOne)
app.route("/manajemen/role/deleteOne", methods=["DELETE"])  (management.roleDeleteOne)

app.route("/manajemen/rolePermission/findAll", methods=["GET"])  (management.rolePermissionFindAll)
app.route("/manajemen/rolePermission/findOne", methods=["GET"])  (management.rolePermissionFindOne)
app.route("/manajemen/rolePermission/insertOne", methods=["POST"])  (management.rolePermissionInsertOne)
app.route("/manajemen/rolePermission/updateOne", methods=["PUT"])  (management.rolePermissionUpdateOne)
app.route("/manajemen/rolePermission/deleteOne", methods=["DELETE"])  (management.rolePermissionDeleteOne)

app.route("/manajemen/permissionAccess/findAll", methods=["GET"])  (management.permissionAccessFindAll)
app.route("/manajemen/permissionAccess/findOne", methods=["GET"])  (management.permissionAccessFindOne)
app.route("/manajemen/permissionAccess/insertOne", methods=["POST"])  (management.permissionAccessInsertOne)
app.route("/manajemen/permissionAccess/updateOne", methods=["PUT"])  (management.permissionAccessUpdateOne)
app.route("/manajemen/permissionAccess/deleteOne", methods=["DELETE"])  (management.permissionAccessDeleteOne)

app.route("/manajemen/bussinesType/findAll", methods=["GET"])  (management.bussinesTypeFindAll)
app.route("/manajemen/bussinesType/findOne", methods=["GET"])  (management.bussinesTypeFindOne)
app.route("/manajemen/bussinesType/insertOne", methods=["POST"])  (management.bussinesTypeInsertOne)
app.route("/manajemen/bussinesType/updateOne", methods=["PUT"])  (management.bussinesTypeUpdateOne)
app.route("/manajemen/bussinesType/deleteOne", methods=["DELETE"])  (management.bussinesTypeDeleteOne)

app.route("/manajemen/menu/findAll", methods=["GET"])  (management.menuFindAll)
app.route("/manajemen/menu/findOne", methods=["GET"])  (management.menuFindOne)
app.route("/manajemen/menu/insertOne", methods=["POST"])  (management.menuInsertOne)
app.route("/manajemen/menu/updateOne", methods=["PUT"])  (management.menuUpdateOne)
app.route("/manajemen/menu/deleteOne", methods=["DELETE"])  (management.menuDeleteOne)

app.route("/manajemen/menuPermissionAccess/findAll", methods=["GET"])  (management.menuPermissionAccessFindAll)
app.route("/manajemen/menuPermissionAccess/findOne", methods=["GET"])  (management.menuPermissionAccessFindOne)
app.route("/manajemen/menuPermissionAccess/insertOne", methods=["POST"])  (management.menuPermissionAccessInsertOne)
app.route("/manajemen/menuPermissionAccess/updateOne", methods=["PUT"])  (management.menuPermissionAccessUpdateOne)
app.route("/manajemen/menuPermissionAccess/deleteOne", methods=["DELETE"])  (management.menuPermissionAccessDeleteOne)

app.route("/manajemen/rolePermissionAccess/findAll", methods=["GET"])  (management.rolePermissionAccessFindAll)
app.route("/manajemen/rolePermissionAccess/findOne", methods=["GET"])  (management.rolePermissionAccessFindOne)
app.route("/manajemen/rolePermissionAccess/insertOne", methods=["POST"])  (management.rolePermissionAccessInsertOne)
app.route("/manajemen/rolePermissionAccess/updateOne", methods=["PUT"])  (management.rolePermissionAccessUpdateOne)
app.route("/manajemen/rolePermissionAccess/deleteOne", methods=["DELETE"])  (management.rolePermissionAccessDeleteOne)