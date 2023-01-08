import httpx
from app.configs  import serviceManagement


def AccessToken(authHeader, userAgent):
    headerJson = {"User-Agent": userAgent, "Authorization": authHeader}
    path = f"{serviceManagement}/token/validate/accessToken"
    responseAPI = httpx.post(path, headers=headerJson)
    responseJson = responseAPI.json()
    return responseJson