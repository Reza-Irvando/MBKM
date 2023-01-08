from http import HTTPStatus
from flask import request
from app import responses
import httpx
from logging import error
from app.configs import serviceManagement


def Login():
    try:
        bodyJson = request.json        
        headerJson = {
            "User-Agent": request.headers["User-Agent"]
        }
        path = f"{serviceManagement}/users/login"
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
    
def Logout():
    try:
        authHeader = request.headers.get("Authorization")
        userAgent = request.headers.get("User-Agent")
        if not authHeader:
            return responses.Make(Status=HTTPStatus.BAD_REQUEST.value,
                                  Message="error",
                                  Data="require token validation."), HTTPStatus.BAD_REQUEST.value
        headerJson = {
            "User-Agent": userAgent,
            "Authorization": authHeader
        }
        path = f"{serviceManagement}/token/validate/accessToken"
        responseAPI = httpx.post(path, headers=headerJson)
        responseJson = responseAPI.json()
        if responseAPI.status_code == HTTPStatus.UNAUTHORIZED.value:
            return responses.Make(
                Status=HTTPStatus.UNAUTHORIZED.value,
                Message="error",
                Data="unauthorized"
            ), HTTPStatus.UNAUTHORIZED.value
        path = f"{serviceManagement}/users/logout/{responseJson['data']['userId']}"
        responseAPI = httpx.delete(path, headers=headerJson)
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
    
def Register():
    try:
        bodyJson = request.json        
        path = f"{serviceManagement}/users/register"
        responseAPI = httpx.post(path, json=bodyJson)
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