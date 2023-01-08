from flask import request
import httpx
from http import HTTPStatus
from app import responses
from logging import error
from app.configs import serviceManagement
from app import validators

def accessFindAll():
    try:
        ### start validasi require token ###
        authHeader = request.headers.get("Authorization")
        userAgent = request.headers.get("User-Agent")
        if not authHeader:
            return responses.Make(
                Status=HTTPStatus.BAD_REQUEST.value,
                Message="error",
                Data="require token validation."), HTTPStatus.BAD_REQUEST.value
        ### stop validasi require token ###

        ### start validasi access token ###
        accessData = validators.AccessToken(authHeader, userAgent)
        if accessData["status"] != 200:
            return responses.Make(
                Status=HTTPStatus.UNAUTHORIZED.value,
                Message="error",
                Data="unauthorized"), HTTPStatus.UNAUTHORIZED.value
        ### stop validasi access token ###
        
        ### start hit service ###
        path = f"{serviceManagement}/manajemen/access/findAll"
        responseAPI = httpx.get(path)
        responseJson = responseAPI.json()
        return responses.Make(Status=responseJson["status"], Message=responseJson["message"], Data=responseJson["data"]), 200
        ### stop hit service ###

    except Exception as err:
        print(err)
        return responses.Make(
            Status=HTTPStatus.INTERNAL_SERVER_ERROR.value,
            Message="error",
            Data=str(err)), HTTPStatus.INTERNAL_SERVER_ERROR.value

def accessFindOne():
    try:
        ### start validasi require token ###
        authHeader = request.headers.get("Authorization")
        userAgent = request.headers.get("User-Agent")
        if not authHeader:
            return responses.Make(
                Status=HTTPStatus.BAD_REQUEST.value,
                Message="error",
                Data="require token validation."), HTTPStatus.BAD_REQUEST.value
        ### stop validasi require token ###

        ### start validasi access token ###
        accessData = validators.AccessToken(authHeader, userAgent)
        if accessData["status"] != 200:
            return responses.Make(
                Status=HTTPStatus.UNAUTHORIZED.value,
                Message="error",
                Data="unauthorized"), HTTPStatus.UNAUTHORIZED.value
        ### stop validasi access token ###
        
        ### start hit service ###
        accessId = request.args["accessId"]
        path = f"{serviceManagement}/manajemen/access/findOne?accessId={accessId}"
        responseAPI = httpx.get(path)
        responseJson = responseAPI.json()
        return responses.Make(Status=responseJson["status"], Message=responseJson["message"], Data=responseJson["data"]), 200
        ### stop hit service ###
        
    except Exception as err:
        print(err)
        return responses.Make(
            Status=HTTPStatus.INTERNAL_SERVER_ERROR.value,
            Message="error",
            Data=str(err)), HTTPStatus.INTERNAL_SERVER_ERROR.value
    
def accessInsertOne():
    try:
        ### start validasi require token ###
        authHeader = request.headers.get("Authorization")
        userAgent = request.headers.get("User-Agent")
        if not authHeader:
            return responses.Make(
                Status=HTTPStatus.BAD_REQUEST.value,
                Message="error",
                Data="require token validation."), HTTPStatus.BAD_REQUEST.value
        ### stop validasi require token ###

        ### start validasi access token ###
        accessData = validators.AccessToken(authHeader, userAgent)
        if accessData["status"] != 200:
            return responses.Make(
                Status=HTTPStatus.UNAUTHORIZED.value,
                Message="error",
                Data="unauthorized"), HTTPStatus.UNAUTHORIZED.value
        ### stop validasi access token ###
        
        ### start hit service ###
        bodyJson = request.json
        path = f"{serviceManagement}/manajemen/access/insertOne"
        responseAPI = httpx.post(path, json=bodyJson)
        responseJson = responseAPI.json()
        return responses.Make(Status=responseJson["status"], Message=responseJson["message"], Data=responseJson["data"]), 200
        ### stop hit service ###
        
    except Exception as err:
        print(err)
        return responses.Make(
            Status=HTTPStatus.INTERNAL_SERVER_ERROR.value,
            Message="error",
            Data=str(err)), HTTPStatus.INTERNAL_SERVER_ERROR.value
    
def accessUpdateOne():
    try:
        ### start validasi require token ###
        authHeader = request.headers.get("Authorization")
        userAgent = request.headers.get("User-Agent")
        if not authHeader:
            return responses.Make(
                Status=HTTPStatus.BAD_REQUEST.value,
                Message="error",
                Data="require token validation."), HTTPStatus.BAD_REQUEST.value
        ### stop validasi require token ###

        ### start validasi access token ###
        accessData = validators.AccessToken(authHeader, userAgent)
        if accessData["status"] != 200:
            return responses.Make(
                Status=HTTPStatus.UNAUTHORIZED.value,
                Message="error",
                Data="unauthorized"), HTTPStatus.UNAUTHORIZED.value
        ### stop validasi access token ###
        
        ### start hit service ###
        accessId = request.args["accessId"]
        bodyJson = request.json
        path = f"{serviceManagement}/manajemen/access/updateOne?accessId={accessId}"
        responseAPI = httpx.put(path, json=bodyJson)
        responseJson = responseAPI.json()
        return responses.Make(Status=responseJson["status"], Message=responseJson["message"], Data=responseJson["data"]), 200
        ### stop hit service ###
        
    except Exception as err:
        print(err)
        return responses.Make(
            Status=HTTPStatus.INTERNAL_SERVER_ERROR.value,
            Message="error",
            Data=str(err)), HTTPStatus.INTERNAL_SERVER_ERROR.value

def accessDeleteOne():
    try:
        ### start validasi require token ###
        authHeader = request.headers.get("Authorization")
        userAgent = request.headers.get("User-Agent")
        if not authHeader:
            return responses.Make(
                Status=HTTPStatus.BAD_REQUEST.value,
                Message="error",
                Data="require token validation."), HTTPStatus.BAD_REQUEST.value
        ### stop validasi require token ###

        ### start validasi access token ###
        accessData = validators.AccessToken(authHeader, userAgent)
        if accessData["status"] != 200:
            return responses.Make(
                Status=HTTPStatus.UNAUTHORIZED.value,
                Message="error",
                Data="unauthorized"), HTTPStatus.UNAUTHORIZED.value
        ### stop validasi access token ###
        
        ### start hit service ###
        accessId = request.args["accessId"]
        path = f"{serviceManagement}/manajemen/access/deleteOne?accessId={accessId}"
        responseAPI = httpx.delete(path)
        responseJson = responseAPI.json()
        return responses.Make(Status=responseJson["status"], Message=responseJson["message"], Data=responseJson["data"]), 200
        ### stop hit service ###
        
    except Exception as err:
        print(err)
        return responses.Make(
            Status=HTTPStatus.INTERNAL_SERVER_ERROR.value,
            Message="error",
            Data=str(err)), HTTPStatus.INTERNAL_SERVER_ERROR.value