from mongoengine import connect
from mongoengine import *
from app import config

connect(alias = 'db_user_management', db = 'db_user_management')

class List(Document):
    # listId = ReferenceField(Roles, required = True)
    ToDoList = StringField(max_length=25, required=True, unique=True)
    Deskripsi = StringField(max_length=100, required=True, unique=True)

    meta = {'db_alias' : 'db_user_management'}