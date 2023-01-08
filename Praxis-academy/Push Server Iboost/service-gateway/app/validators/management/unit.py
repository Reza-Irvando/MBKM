from json_checker import Checker
def UnitRegister(data):
    try:       
        checker = Checker({
            "companyName": str,
            "companyEmail": str,
            "companyPhone": str,
            "password": str,
            "personResponsibleName": str,
            "personResponsibleContact": str,
            "contractValue": float,
            "contractActiveDateStart": str,
            "contractActiveDateEnd": str,
            "channelDeals": [
                {
                    "platform": str,
                    "price": float,
                    "effectiveStartDate": str,
                    "effectiveEndDate": str
                }
            ]
        })
        checker.validate(data)
        return False
    except Exception as err:
        return err