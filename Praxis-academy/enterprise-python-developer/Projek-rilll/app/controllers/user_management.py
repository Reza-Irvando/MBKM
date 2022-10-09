from flask import request
from app import validators
from http import HTTPStatus
from app import response
from app import models

def AddList():
    bodyJson = request.json
    err = validators.AddList(bodyJson)
    if err:
        return response.Make(
            Status = HTTPStatus.BAD_REQUEST.value,
            Message = "error",
            Data = str(err)
            ), HTTPStatus.BAD_REQUEST.value
    
    collList = models.List(
        ToDoList = bodyJson["ToDoList"], Deskripsi = bodyJson["Deskripsi"])
    
    collList.save()
    return response.Make(
        Status = HTTPStatus.OK.value,
        Message = "success",
        Data = f"To Do List {bodyJson['ToDoList']} has added"
    ), HTTPStatus.OK.value

def ViewList():
    collList = models.List.objects().all()
    data = []
    for i in collList:
        data.append({
            "id": str(i.id),
            "ToDoList": i.ToDoList,
            "Deskripsi": i.Deskripsi,
        })
    print(collList)
    return response.Make(
        Status=HTTPStatus.OK.value,
        Message="success",
        Data=data
    ), HTTPStatus.OK.value

def UpdateList(listId):
    bodyJson = request.json
    err = validators.UpdateList(bodyJson)
    if err:
        return response.Make(
            Status = HTTPStatus.BAD_REQUEST.value,
            Message = "error",
            Data = str(err)
        ), HTTPStatus.BAD_REQUEST.value
    
    collList = models.List.objects(id = listId).update(ToDoList=bodyJson["ToDoList"], Deskripsi=bodyJson["Deskripsi"])
    print(collList)
    return(bodyJson)

def DeleteList():
    listId = request.args["listId"]
    models.List.objects(id = listId).delete()
    return response.Make(
        Status = HTTPStatus.BAD_REQUEST.value,
        Message = "error",
        Data = f"successfuly deleted list : {listId}"
    ), HTTPStatus.OK.value

def DetailList(listId):
    collList = models.List.objects(id = listId).first()
    if not collList:
        return response.Make(
            Status=HTTPStatus.OK.value,
            Message="error",
            Data="Tidak Ditemukan."
        ), HTTPStatus.BAD_REQUEST.value
    return response.Make(
        Status=HTTPStatus.OK.value,
        Message="success",
        Data={
            "ToDoList": collList.ToDoList,
            "Deskripsi": collList.Deskripsi
        }
    ), HTTPStatus.OK.value