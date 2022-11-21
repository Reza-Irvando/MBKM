from flask import request
from app import validators
from http import HTTPStatus
from app import responses
from app import models
from bson import ObjectId

def Regist():
    bodyJson = request.json
    err = validators.AddList(bodyJson)
    if err:
        return responses.Make(
            Status = HTTPStatus.BAD_REQUEST.value,
            Message = "error",
            Data = str(err)
            ), HTTPStatus.BAD_REQUEST.value
    
    collList = models.List(
        ToDoList = bodyJson["ToDoList"], Deskripsi = bodyJson["Deskripsi"])
    
    collList.save()
    return responses.Make(
        Status = HTTPStatus.OK.value,
        Message = "success",
        Data = f"To Do List {bodyJson['ToDoList']} has added"
    ), HTTPStatus.OK.value

def List():
    collList = models.List.objects().all()
    data = []
    for i in collList:
        data.append({
            "id": str(i.id),
            "ToDoList": i.ToDoList,
            "Deskripsi": i.Deskripsi,
        })
    print(collList)
    return responses.Make(
        Status=HTTPStatus.OK.value,
        Message="success",
        Data=data
    ), HTTPStatus.OK.value

def Analytic():
    listId = request.args["id"]
    print(listId)
    bodyJson = request.json
    err = validators.UpdateList(bodyJson)
    if err:
        return responses.Make(
            Status = HTTPStatus.BAD_REQUEST.value,
            Message = "error",
            Data = str(err)
        ), HTTPStatus.BAD_REQUEST.value
  
    collList = models.List.objects(id = ObjectId(listId)).update(ToDoList=bodyJson["ToDoList"], Deskripsi=bodyJson["Deskripsi"])
    print(collList)
    return(bodyJson)

def Topup():
    listId = request.args["id"]
    collList = models.List.objects(id = ObjectId(listId)).delete()
    if not collList:
        return responses.Make(
            Status=HTTPStatus.OK.value,
            Message="error",
            Data="Tidak Ditemukan."
        ), HTTPStatus.BAD_REQUEST.value
    return responses.Make(
        Status = HTTPStatus.BAD_REQUEST.value,
        Message = "success",
        Data = f"successfuly deleted list : {listId}"
    ), HTTPStatus.OK.value

def Split():
    listId = request.args["id"]
    collList = models.List.objects(id = ObjectId(listId)).first()
    if not collList:
        return responses.Make(
            Status=HTTPStatus.OK.value,
            Message="error",
            Data="Tidak Ditemukan."
        ), HTTPStatus.BAD_REQUEST.value
    return responses.Make(
        Status=HTTPStatus.OK.value,
        Message="success",
        Data={
            "ToDoList": collList.ToDoList,
            "Deskripsi": collList.Deskripsi
        }
    ), HTTPStatus.OK.value

def Approval():
    listId = request.args["id"]
    collList = models.List.objects(id = ObjectId(listId)).first()
    if not collList:
        return responses.Make(
            Status=HTTPStatus.OK.value,
            Message="error",
            Data="Tidak Ditemukan."
        ), HTTPStatus.BAD_REQUEST.value
    return responses.Make(
        Status=HTTPStatus.OK.value,
        Message="success",
        Data={
            "ToDoList": collList.ToDoList,
            "Deskripsi": collList.Deskripsi
        }
    ), HTTPStatus.OK.value

def History():
    listId = request.args["id"]
    collList = models.List.objects(id = ObjectId(listId)).first()
    if not collList:
        return responses.Make(
            Status=HTTPStatus.OK.value,
            Message="error",
            Data="Tidak Ditemukan."
        ), HTTPStatus.BAD_REQUEST.value
    return responses.Make(
        Status=HTTPStatus.OK.value,
        Message="success",
        Data={
            "ToDoList": collList.ToDoList,
            "Deskripsi": collList.Deskripsi
        }
    ), HTTPStatus.OK.value