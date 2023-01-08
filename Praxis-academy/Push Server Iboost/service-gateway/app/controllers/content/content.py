from flask import request
import httpx
from http import HTTPStatus
from app import responses
from logging import error
from app.configs import serviceManagement
from app.configs import serviceMaster
from app.configs import serviceContent
from app import validators

def ContentList():
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
        path = f"{serviceContent}/content/list"
        responseAPI = httpx.get(path)
        responseJson = responseAPI.json()
        return responses.Make(Status=responseJson["status"], Message=responseJson["message"], Data=responseJson["data"]), 200
        ### stop hit service ###
    except Exception as err:
        error(err)
        return responses.Make(
            Status=HTTPStatus.INTERNAL_SERVER_ERROR.value,
            Message="error",
            Data=str(err)), HTTPStatus.INTERNAL_SERVER_ERROR.value

def ContentCreate():
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
        # err = validators.BudgetUnitTopUp(bodyJson)
        # if err:
        #     return responses.Make(
        #         Status=HTTPStatus.BAD_REQUEST.value,
        #         Message="error",
        #         Data=str(err)
        #     ), HTTPStatus.BAD_REQUEST.value
        path = f"{serviceContent}/content/create?userId={accessData['data']['userId']}"
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

def ContentApprove():
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
        contentId = request.args["contentId"]
        path = f"{serviceContent}/content/approve?contentId={contentId}"
        responseAPI = httpx.put(path, json=bodyJson)
        responseJson = responseAPI.json()
        return responses.Make(Status=responseJson["status"], Message=responseJson["message"], Data=responseJson["data"]), 200
        ### stop hit service ###

    except Exception as err:
        error(err)
        return responses.Make(
            Status=HTTPStatus.INTERNAL_SERVER_ERROR.value,
            Message="error",
            Data=str(err)), HTTPStatus.INTERNAL_SERVER_ERROR.value

def ContentReject():
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
        contentId = request.args["contentId"]
        path = f"{serviceContent}/content/reject?userId={accessData['data']['userId']}&contentId={contentId}"
        responseAPI = httpx.put(path, json=bodyJson)
        responseJson = responseAPI.json()
        return responses.Make(Status=responseJson["status"], Message=responseJson["message"], Data=responseJson["data"]), 200
        ### stop hit service ###

    except Exception as err:
        error(err)
        return responses.Make(
            Status=HTTPStatus.INTERNAL_SERVER_ERROR.value,
            Message="error",
            Data=str(err)), HTTPStatus.INTERNAL_SERVER_ERROR.value

def ContentRevision():
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
        contentId = request.args["contentId"]
        path = f"{serviceContent}/content/revision?userId={accessData['data']['userId']}&contentId={contentId}"
        responseAPI = httpx.put(path, json=bodyJson)
        responseJson = responseAPI.json()
        return responses.Make(Status=responseJson["status"], Message=responseJson["message"], Data=responseJson["data"]), 200
        ### stop hit service ###

    except Exception as err:
        error(err)
        return responses.Make(
            Status=HTTPStatus.INTERNAL_SERVER_ERROR.value,
            Message="error",
            Data=str(err)), HTTPStatus.INTERNAL_SERVER_ERROR.value