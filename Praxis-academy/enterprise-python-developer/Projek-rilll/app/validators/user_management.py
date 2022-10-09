from json_checker import Checker

def AddList(request):
    try:
        schema = {
            "ToDoList": str,
            "Deskripsi": str
        }
        checker = Checker(schema)
        checker.validate(request)
        return False 
    except Exception as err:
        return err

def UpdateList(data):
    try:
        checker = Checker({
            "ToDoList": str,
            "Deskripsi": str
        })
        checker.validate(data)
        return False
    except Exception as err:
        return err

def DeleteList(data):
    try:
        checker = Checker({
            "ToDoList": str,
            "Deskripsi": str
        })
        checker.validate(data)
        return False
    except Exception as err:
        return err