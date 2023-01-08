from json_checker import Checker, Or


def ContentCreate(data):
    try:
        checker = Checker({
            "platformCode": str,
            "contentMessage": dict,
            "payloadMessage": dict,
            "contentDuration": int,
            "segment": Or(str, dict),
            "contentEstimateTarget": int,
            "contentPrice": float
        })
        checker.validate(data)
        return False
    except Exception as err:
        return err
