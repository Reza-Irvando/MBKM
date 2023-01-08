from json_checker import Checker
def UserRegister(data):
    try:       
        checker = Checker({
            "userName": str,
            "userPassword": str,
            "userEmail": str,
            "userPhoneNumber": str,
        })
        checker.validate(data)
        return False
    except Exception as err:
        return err