from flask import jsonify, request
from app import validators
from app import response
from http import HTTPStatus
from app import models

def index() :
    data = [
        {
        "id" : 1,
        "name" : "Adi"
    },
    {
        "id" : 2,
        "name" : "Ado"
    }
    ]
    return jsonify(data) 

def create():
    bodyJson = request.json
    err = validators.tes(bodyJson)
    if err:
        return response.Make(
            Status=HTTPStatus.BAD_REQUEST.value,
            Message = "error",
            Data = str(err)
        ), HTTPStatus.BAD_REQUEST.value
    
    collUser = models.User(userName = bodyJson["userName"], userPassword = bodyJson["userPassword"])
    collUser.save()
    return response.Make(
        Status = HTTPStatus.OK.value,
        Message = "success",
        Data = {}
    ),HTTPStatus.OK.value