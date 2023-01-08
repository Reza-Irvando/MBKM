from logging import error
from app import responses
from http import HTTPStatus
from app import models
from flask import request
from bson import ObjectId
from app import validators

def ContentList():
    try:
        accountId = ObjectId(request.args["accountId"])
        collUserUnitRoles = models.UserUnitRoles.objects(id=accountId).first()
        roleName = collUserUnitRoles.unitRoleId.roleId.roleName
        
        if roleName == "UNIT DIRECTOR":
            collUserUnitRoles = models.UserUnitRoles.objects(id=accountId).first()
            unitId = collUserUnitRoles.unitRoleId.unitId.id
            collUserUnitRoles = models.UserUnitRoles.objects(unitId=unitId)
            data = []
            for i in collUserUnitRoles:
                data.append(i.id)
            collContent = models.Contents.objects(createdBy__in=data)
            
        elif roleName == "UNIT MANAGER":
            collUserUnitRoles = models.UserUnitRoles.objects(createdBy=accountId)
            data = []
            for i in collUserUnitRoles:
                data.append(i.id)
            collContent = models.Contents.objects(createdBy__in=data)
            
        else:
            collContent = models.Contents.objects(createdBy=accountId)
            
        data = []
        for d in collContent:
            data.append({
                "contentId": str(d.id),
                "contentName": d.contentName
            })
        return responses.Make(
            Status=200,
            Message="success",
            Data=data
        ), 200
    except Exception as err:
        error(err)
        return responses.Make(
            Status=HTTPStatus.INTERNAL_SERVER_ERROR.value,
            Message="error",
            Data=str(err)), HTTPStatus.INTERNAL_SERVER_ERROR.value

def ContentCreate():
    try:
        bodyJson = request.json
        accountId = ObjectId(request.args["accountId"])
        err = validators.ContentCreate(bodyJson)
        if err:
            return responses.Make(
                Status=HTTPStatus.BAD_REQUEST.value,
                Message="error",
                Data=str(err)
            ), HTTPStatus.BAD_REQUEST.value
        
        if type(bodyJson["segment"]) == str:
            collSegment = models.Segments.objects(id=ObjectId(bodyJson["segment"])).first()
        else:
            collSegment = models.Segments(
                segmentName=bodyJson["segment"]["segmentTitle"],
                segmentAge=bodyJson["segment"]["ageSegments"],
                segmentClass=bodyJson["segment"]["classSegments"],
                segmentGender=bodyJson["segment"]["genderSegments"],
                segmentInterest=bodyJson["segment"]["interestSegments"],
                segmentLocation=bodyJson["segment"]["locations"],
                createdBy=accountId,
                updatedBy=accountId,
            )
            collSegment.save()
            
        collPaymentStatus = models.PaymentStatus.objects(paymentStatusCode="unpaid").first()
        collMutationPaymentStatus = models.MutationPaymentStatus(
            paymentStatusId=collPaymentStatus,
            createdBy=accountId,
            updatedBy=accountId,
        )
        collMutationPaymentStatus.save()
        
        collBlastStatus = models.BlastStatus.objects(blastStatusCode="review").first()
        collPlatform = models.Platforms.objects(platformCode=bodyJson["platformCode"]).first()
        collContent = models.Contents(
            payloadMessage=bodyJson["contentMessage"],
            contentName=bodyJson["contentMessage"]["title"],
            contentMessage=bodyJson["payloadMessage"],
            contentEstimateTarget=bodyJson["contentEstimateTarget"],
            contentDuration=bodyJson["contentDuration"],
            contentPrice=bodyJson["contentPrice"],
            platformId=collPlatform,
            blastStatusId=collBlastStatus,
            paymentStatus=collMutationPaymentStatus,
            segmentId=collSegment,
            createdBy=accountId,
            updatedBy=accountId,
        )
        collContent.save()
        
        collContentBlastStatus = models.ContentBlastStatus(
            contentId=collContent,
            blastStatusId=collBlastStatus,
            createdBy=accountId,
            updatedBy=accountId,
        )
        collContentBlastStatus.save()
        
        return responses.Make(
            Status=200,
            Message="success",
            Data={
                "contentId":str(collContent.id),
                "contentEstimateTarget": collContent.contentEstimateTarget,
                "contentDuration": collContent.contentDuration,
                "contentPrice": collContent.contentPrice,
                "platform": collPlatform.platformName,
                "paymentStatus": collPaymentStatus.paymentStatusName,
                "segmentId": str(collSegment.id)
            }
        ), 200
    
    except Exception as err:
        error(err)
        return responses.Make(
            Status=HTTPStatus.INTERNAL_SERVER_ERROR.value,
            Message="error",
            Data=str(err)), HTTPStatus.INTERNAL_SERVER_ERROR.value
    
