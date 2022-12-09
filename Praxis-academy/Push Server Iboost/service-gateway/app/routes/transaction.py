from app import app
from app.controllers import transaction

app.route("/transaction/unit/budget/topUp",
          methods=["POST"])(transaction.budgetTopUp)

app.route("/transaction/unit/budget/balance",
          methods=["GET"])(transaction.UnitBudgetBalance)

app.route("/transaction/unit/budget/allocation",
          methods=["POST"])(transaction.UnitBudgetAllocation)