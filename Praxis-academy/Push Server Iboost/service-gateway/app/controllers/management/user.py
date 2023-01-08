from flask import request
import httpx
from http import HTTPStatus
from app import responses
from logging import error
from app.configs import serviceManagement
from app.validators import management as ValidManage
from app import validators

def UserRegister():
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

        ### start validasi permission ###
        permHost = request.headers["Host"]
        permPath = request.url_rule
        permMeth = request.method
        permissionData = validators.Permission(accessData, permHost, permPath,
                                               permMeth)
        if permissionData["status"] != 200:
            return responses.Make(
                Status=HTTPStatus.UNAUTHORIZED.value,
                Message="error",
                Data="unauthorized"), HTTPStatus.UNAUTHORIZED.value
        ### stop validasi permission ###

        ### start hit service ###
        bodyJson = request.json
        err = ValidManage.UserRegister(bodyJson)
        if err:
            return responses.Make(
                Status=HTTPStatus.BAD_REQUEST.value,
                Message="error",
                Data=str(err)
            ), HTTPStatus.BAD_REQUEST.value

        path = f"{serviceManagement}/management/user/register?userId={accessData['data']['userId']}&roleId={accessData['data']['roleId']}"
        responseAPI = httpx.post(path, json=bodyJson)
        responseJson = responseAPI.json()
        return responses.Make(Status=responseJson["status"], Message=responseJson["message"], Data=responseJson["data"]), 200
        ### stop hit service ###
    except Exception as err:
        error(err)
        return responses.Make(
            Status=HTTPStatus.INTERNAL_SERVER_ERROR.value,
            Message="error",
            Data=str(err)), HTTPStatus.INTERNAL_SERVER_ERROR.value