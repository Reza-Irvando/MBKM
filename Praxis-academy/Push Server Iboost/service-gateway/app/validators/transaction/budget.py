from json_checker import Checker
def BudgetUnitAllocation(data):
    try:       
        checker = Checker({
            "toAccountId": str,
            "budgetAmount": float,
            "mutationNote": str,
            "userPin": str
        })
        checker.validate(data)
        return False
    except Exception as err:
        return err