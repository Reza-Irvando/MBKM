from json_checker import Checker

def Register(data):
    try:
        checker = Checker({
            'userName' : str,
            'userPassword' : str,
            'userEmail' : str
        })
        checker.validate(data)
        return False
    except Exception as err:
        return err