from app import app
from app.controllers import master

app.route("/master/paymentStatus/list",    methods=["GET"])   (master.PaymentStatusList)
app.route("/master/paymentStatus/create",      methods=["POST"])   (master.PaymentStatusCreate)
app.route("/master/paymentStatus/delete",         methods=["DELETE"])   (master.PaymentStatusDelete)
app.route("/master/paymentStatus/update",        methods=["PUT"])   (master.PaymentStatusUpdate)
app.route("/master/paymentStatus/detail",    methods=["GET"])   (master.PaymentStatusDetail)