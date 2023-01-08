from app import app
from app.controllers import master

app.route("/master/paymentStatus/list",    methods=["GET"]) (master.PaymentStatusList)
app.route("/master/paymentStatus/create",      methods=["POST"])    (master.PaymentStatusCreate)
app.route("/master/paymentStatus/delete",         methods=["DELETE"])   (master.PaymentStatusDelete)
app.route("/master/paymentStatus/update",        methods=["PUT"])   (master.PaymentStatusUpdate)
app.route("/master/paymentStatus/detail",    methods=["GET"])   (master.PaymentStatusDetail)
app.route("/master/bank/list",   methods=["GET"])   (master.BankList)
app.route("/master/bank/create",   methods=["POST"])    (master.BankCreate)
app.route("/master/bank/detail",   methods=["GET"]) (master.BankDetail)
app.route("/master/bank/update",   methods=["PUT"]) (master.BankUpdate)
app.route("/master/bank/delete",   methods=["DELETE"])  (master.BankDelete)
app.route ("/master/category/list", methods = ["GET"])(master.CategoryList)
app.route ("/master/category/create", methods = ["POST"])(master.CategoryCreate)
app.route ("/master/category/detail", methods = ["GET"])(master.CategoryDetail)
app.route ("/master/category/update", methods = ["PUT"])(master.CategoryUpdate)
app.route ("/master/category/delete", methods = ["DELETE"])(master.CategoryDelete)
app.route ("/master/blastStatus/list", methods = ["GET"])(master.BlastStatusList)
app.route ("/master/blastStatus/create", methods = ["POST"])(master.BlastStatusCreate)
app.route ("/master/blastStatus/detail", methods = ["GET"])(master.BlastStatusDetail)
app.route ("/master/blastStatus/update", methods = ["PUT"])(master.BlastStatusUpdate)
app.route ("/master/blastStatus/delete", methods = ["DELETE"])(master.BlastStatusDelete)
app.route("/master/platform/list",   methods=["GET"])(master.PlatformList)
app.route("/master/platform/create",   methods=["POST"])(master.PlatformCreate)
app.route("/master/platform/detail",   methods=["GET"])(master.PlatformDetail)
app.route("/master/platform/update",   methods=["PUT"])(master.PlatformUpdate)
app.route("/master/platform/delete",   methods=["DELETE"])(master.PlatformDelete)