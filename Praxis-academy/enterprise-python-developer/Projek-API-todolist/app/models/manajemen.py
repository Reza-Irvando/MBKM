from mongoengine import *
connect('mydb')

def Role(Document):
    rolename = StringField()

def User(Document):
    userName = StringField()
    userPassword = StringField()
    # role = ReferenceField(Role, null=)