from flask import request
import httpx
from http import HTTPStatus
from app import responses
from logging import error
from app.configs import serviceManagement
from app import validators

def accountLogin():
    try:
        bodyJson = request.json        
        headerJson = {
            "User-Agent": request.headers["User-Agent"]
        }
        path = f"{serviceManagement}/manajemen/account/login"
        responseAPI = httpx.post(path, json=bodyJson, headers=headerJson)
        responseJson = responseAPI.json()
        return responses.Make(
                Status=responseJson["status"],
                Message=responseJson["message"],
                Data=responseJson["data"]
            ), responseAPI.status_code
    except Exception as err:
        error(err)
        return responses.Make(
            Status=HTTPStatus.INTERNAL_SERVER_ERROR.value,
            Message="error",
            Data=str(err)
        ), HTTPStatus.INTERNAL_SERVER_ERROR.value
        
def accountRegisterCORP():
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
        path = f"{serviceManagement}/manajemen/account/registerCorp"
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

def accountRegisterDB():
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
        path = f"{serviceManagement}/manajemen/account/registerCorpDb"
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
        
def accountRegisterSmb():
    try:
        bodyJson = request.json        
        headerJson = {
            "User-Agent": request.headers["User-Agent"]
        }
        path = f"{serviceManagement}/manajemen/account/registerSmb"
        responseAPI = httpx.post(path, json=bodyJson, headers=headerJson)
        responseJson = responseAPI.json()
        return responses.Make(
                Status=responseJson["status"],
                Message=responseJson["message"],
                Data=responseJson["data"]
            ), responseAPI.status_code
    except Exception as err:
        error(err)
        return responses.Make(
            Status=HTTPStatus.INTERNAL_SERVER_ERROR.value,
            Message="error",
            Data=str(err)
        ), HTTPStatus.INTERNAL_SERVER_ERROR.value