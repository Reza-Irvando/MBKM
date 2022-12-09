import httpx
from app.configs import serviceManagement

def Permission(accessData, permHost, permPath, permMeth):
    path = f"{serviceManagement}/permission/validate?userId={accessData['data']['userId']}&roleId={accessData['data']['roleId']}"
    responseAPI = httpx.post(path, json={
		"method": str(permMeth),
		"path": str(permPath)
	})
    responseJson = responseAPI.json()
    return responseJson