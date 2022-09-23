from flask import request
from app import validators
from http import HTTPStatus
from app import response
from app import models

def Register():
    bodyJson = request.json
    err = validators.Register(bodyJson)
    if err:
        return response.Make(
            Status = HTTPStatus.BAD_REQUEST.value,
            Message = "error",
            Data = str(err)
        ), HTTPStatus.BAD_REQUEST.value
    
    collUser = models.Users(
        userName = bodyJson["userName"],
        userPassword = bodyJson["userPassword"],
        userEmail = bodyJson("userEmail"),
        roleId = bodyJson["roleId"]
    )
    return response.Make(
            Status = HTTPStatus.OK.value,
            Message = "error",
            Data = f"user {bodyJson['userName']} has created"
    ), HTTPStatus.OK.value

def Login():
    bodyJson = request.json
    collUser = models.Users.objects(userName=bodyJson["userName"], userPassword = bodyJson["userPassword"]).first()
    print(collUser)
    return response.Make(
            Status = HTTPStatus.OK.value,
            Message = "success",
            Data = {
                "userName": collUser.userName,
                "userEmail": collUser.userEmail
            }
    ), HTTPStatus.OK.value
