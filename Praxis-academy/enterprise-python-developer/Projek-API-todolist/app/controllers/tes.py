from flask import jsonify, request
from app import validators

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
    print(err)
    return ""