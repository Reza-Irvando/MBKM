from json_checker import Checker

request = {
    "userName" : "adi",
    "userPassword" : "secret"
}

def tes(request):
    try:
        schema = {
            "userName" : int,
            "userPassword" : str
        }
        checker = Checker(schema)
        checker.validate(request)
        return False
    except Exception as err:
        return err
        # print(err)
# tes(request)