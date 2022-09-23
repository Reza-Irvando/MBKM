from ast import alias
from typing_extensions import Required
from mongoengine import connect
from mongoengine import *
from datetime import datetime
fom app import config

connect(alias = 'db_user_management', db = 'db_user_management')

class Roles(Document):
    roleName = StringField(required=True, unique=True)
    meta = {'db_alias': 'db_user_management'}

class Users(Document):
    roleId = ReferenceField()
    userName = StringField(max_length=25, required=True, unique=True)
    userEmail = EmailField(required=True, unique=True)
    userPassword = StringField(required=True)
    userFirstName = StringField(max_length=25)
    userLastName = StringField(max_length=25)
    userPhoneNumber = StringField(max_length=15, required=True, unique=True)
    createdAt = DateTimeField(required=True, default=datetime.utcnow)
    updateAt = DateTimeField(required=True, default=datetime.utcnow)
    updateBy = ReferenceField("self", null=True)
    createdBy = ReferenceField("self", null=True)
    isActive = BooleanField(required=True, default=True)
    isDelete = BooleanField(required=True, default=False)

    meta = {'db_alias' : 'db_user_management'}

    array = ["DOSEN", "MAHASISWA"]
    for d in array:
        coll = Roles(rolename=d)
        coll.save()