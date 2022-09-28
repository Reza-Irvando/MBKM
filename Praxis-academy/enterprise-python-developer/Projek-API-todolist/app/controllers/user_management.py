from email.message import Message
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
    print(collUser.roleId.roleName)
    if not collUser:
        return response.Make(
            Status = HTTPStatus.BAD_REQUEST.value,
            Message = "error",
            Data = "user doesn't exist."
        ), HTTPStatus.BAD_REQUEST.value
    return response.Make(
        Status = HTTPStatus.OK.value,
        Message = "success",
            Data = {
            "userName": collUser.userName,
            "userEmail": collUser.userEmail
        }
    ), HTTPStatus.OK.value

def ListUser():
    collUser = models.Users.objects.all()
    
    data = []
    for i in collUser:
        data.append({
            "id" : i.collUser.id,
            "userName" : i.collUser.userName,
            "userEmail" : i.collUser.userEmail,
            "userRole" : i.collUser.roleId.roleName
        })
    print(collUser)
    return response.Make(
        Status = HTTPStatus.OK.value,
        Message = "success",
        Data = ""
    ), HTTPStatus.OK.value

def UpdateUser():
    bodyJson = request.json
    err = validators.UpdateUser(bodyJson)
    if err:
        return response.Make(
            Status = HTTPStatus.BAD_REQUEST.value,
            Message = "error",
            Data = str(err)
        ), HTTPStatus.BAD_REQUEST.value
    
    collUser = models.Users.objects(id = userId).update(userEmail=bodyJson["userEmail"])
    print(collUser)
    return(bodyJson)

def DeleteUser():
    userId = request.args["userId"]
    models.Users.objeccts(id = userId).delete()
    return response.Make(
        Status = HTTPStatus.BAD_REQUEST.value,
        Message = "error",
        Data = f"successfuly deleted user with id : {userId}"
    ), HTTPStatus.OK.value