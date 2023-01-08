from flask import request
import httpx
from http import HTTPStatus
from app import responses
from logging import error
from app.configs import serviceManagement

def Profile():
    try:
        authHeader = request.headers.get("Authorization")
        userAgent = request.headers.get("User-Agent")
        if not authHeader:
            return responses.Make(Status=HTTPStatus.BAD_REQUEST.value,
                                  Message="error",
                                  Data="require token validation."), HTTPStatus.BAD_REQUEST.value
        headerJson = {"User-Agent": userAgent, "Authorization": authHeader}
        path = f"{serviceManagement}/token/validate/accessToken/"
        responseAPI = httpx.post(path, headers=headerJson)
        responseJson = responseAPI.json()
        if responseAPI.status_code == HTTPStatus.UNAUTHORIZED.value:
            return responses.Make(
                Status=HTTPStatus.UNAUTHORIZED.value,
                Message="error",
                Data="unauthorized"
            ), HTTPStatus.UNAUTHORIZED.value

        permHost = request.headers["Host"]
        permPath = request.url_rule
        permMeth = request.method
        print(permHost)
        print(permPath)
        print(permMeth)
        if permHost == "127.0.0.1:8080":
            print("sesuai")
        # return asyncio.run(
        #     requestWrapper.Get(
        #         f"{serviceManagement}/users/profile/{authResponseJson['userId']}"
        #     ))
        path = f"{serviceManagement}/users/profile/{responseJson['data']['userId']}"
        responseAPI = httpx.get(path, headers=headerJson)
        responseJson = responseAPI.json()
        return responses.Make(
                Status=responseJson["status"],
                Message=responseJson["message"],
                Data=responseJson["data"]
            ), responseAPI.status_code
    except Exception as err:
        error(err)
        return responses.Make(Status=HTTPStatus.INTERNAL_SERVER_ERROR.value,
                                  Message="error",
                                  Data=str(err)), HTTPStatus.INTERNAL_SERVER_ERROR.value