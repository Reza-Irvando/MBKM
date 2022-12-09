from flask import request
from app import responses
from http import HTTPStatus
import httpx
from logging import error
from app.configs import serviceManagement

def RefreshToken():
    try:
        authHeader = request.headers.get("Authorization")
        userAgent = request.headers.get("User-Agent")
        if not authHeader:
            return responses.Make(Status=HTTPStatus.BAD_REQUEST.value,
                                  Message="error",
                                  Data="require token validation."), HTTPStatus.BAD_REQUEST.value
        print("authHeader: ", authHeader)
        print("userAgent: ", userAgent)
        headerJson = {
            "User-Agent": userAgent,
            "Authorization": authHeader
        }
        path = f"{serviceManagement}/token/refresh"
        responseAPI = httpx.post(path, headers=headerJson)
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
            Data=str(err)), HTTPStatus.INTERNAL_SERVER_ERROR.value