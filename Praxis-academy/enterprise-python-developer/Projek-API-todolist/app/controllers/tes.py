from flask import jsonify, request
from app import validators
from app import response
from http import HTTPStatus

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
        )
    # print(err)
    return response.Make(
        Status = HTTPStatus.OK.value,
        Message = "success",
        Data = {}
    )