from flask import request
import httpx
from http import HTTPStatus
from app import responses
from logging import error
from app.configs import serviceManagement
from app.configs import serviceMaster
from app import validators

def PaymentStatusList():
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
        path = f"{serviceMaster}/master/paymentStatus/list"
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

def PaymentStatusCreate():
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
        path = f"{serviceMaster}/master/paymentStatus/create?userId={accessData['data']['userId']}"
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

def PaymentStatusDetail():
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
        paymentStatusId = request.args["paymentStatusId"]
        path = f"{serviceMaster}/master/paymentStatus/detail?paymentStatusId={paymentStatusId}"
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

def PaymentStatusUpdate():
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
        paymentStatusId = request.args["paymentStatusId"]
        path = f"{serviceMaster}/master/paymentStatus/update?userId={accessData['data']['userId']}&paymentStatusId={paymentStatusId}"
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

def PaymentStatusDelete():
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
        paymentStatusId = request.args["paymentStatusId"]
        path = f"{serviceMaster}/master/paymentStatus/delete?userId={accessData['data']['userId']}&paymentStatusId={paymentStatusId}"
        responseAPI = httpx.delete(path)
        responseJson = responseAPI.json()
        return responses.Make(Status=responseJson["status"], Message=responseJson["message"], Data=responseJson["data"]), 200
        ### stop hit service ###

    except Exception as err:
        error(err)
        return responses.Make(
            Status=HTTPStatus.INTERNAL_SERVER_ERROR.value,
            Message="error",
            Data=str(err)), HTTPStatus.INTERNAL_SERVER_ERROR.value