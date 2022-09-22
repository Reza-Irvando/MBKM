from json_checker import Checker

request = {
    "userName" : "adi",
    "userPassword" : "secret"
}

def tes(request):
    try:
        schema = {
            "userName" : str,
            "userPassword" : str
        }
        checker = Checker(schema)
        checker.validate(request)
        return True
    except Exception as err:
        return err
        # print(err)
# tes(request)