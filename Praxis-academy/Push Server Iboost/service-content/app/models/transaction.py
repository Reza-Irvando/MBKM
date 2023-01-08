from mongoengine import connect
from mongoengine import *
from datetime import datetime
from .management import Users
from app import configs
from .management import Units
from .management import UserUnitRoles
from .master import PaymentStatus

connect(alias='transaction', db=configs.mongoDbTransaction, host=configs.mongoHost, port=configs.mongoPort)

class Budgets(Document):
    unitId = ReferenceField(Units, required=True)
    budgetDC = StringField(required=True)
    budgetAmount = DecimalField(required=True, min_value=0, precision=2)
    createdAt = DateTimeField(required=True, default=datetime.utcnow())
    updatedAt = DateTimeField(required=True, default=datetime.utcnow())
    updatedBy = ReferenceField(Users, null=True)
    createdBy = ReferenceField(Users, null=True)
    isActive = BooleanField(required=True, default=True)
    isDelete = BooleanField(required=True, default=False)
    
    meta = {'db_alias': 'transaction'}
    
class Mutations(Document):
    fromUserUnitRoleId = ReferenceField(UserUnitRoles, required=True)
    toUserUnitRoleId = ReferenceField(UserUnitRoles, required=True)
    mutationAmount = DecimalField(required=True, min_value=0, precision=2)
    mutationNote = StringField()
    createdAt = DateTimeField(required=True, default=datetime.utcnow())
    updatedAt = DateTimeField(required=True, default=datetime.utcnow())
    updatedBy = ReferenceField(Users, null=True)
    createdBy = ReferenceField(Users, null=True)
    isActive = BooleanField(required=True, default=True)
    isDelete = BooleanField(required=True, default=False)
    
    meta = {'db_alias': 'transaction'}
    
class Wallets(Document):
    walletDC = StringField(required=True)
    walletAmount = DecimalField(required=True, min_value=0, precision=2)
    userUnitRoleId = ReferenceField(UserUnitRoles, required=True)
    mutationId = ReferenceField(Mutations, required=True)
    createdAt = DateTimeField(required=True, default=datetime.utcnow())
    updatedAt = DateTimeField(required=True, default=datetime.utcnow())
    updatedBy = ReferenceField(Users, null=True)
    createdBy = ReferenceField(Users, null=True)
    isActive = BooleanField(required=True, default=True)
    isDelete = BooleanField(required=True, default=False)
    
    meta = {'db_alias': 'transaction'}
    
class MutationPaymentStatus(Document):
    mutationId = ReferenceField(Mutations, null=True)
    paymentStatusId = ReferenceField(PaymentStatus, required=True)
    createdAt = DateTimeField(required=True, default=datetime.utcnow())
    updatedAt = DateTimeField(required=True, default=datetime.utcnow())
    updatedBy = ReferenceField(UserUnitRoles, null=True)
    createdBy = ReferenceField(UserUnitRoles, null=True)
    isActive = BooleanField(required=True, default=True)
    isDelete = BooleanField(required=True, default=False)
    
    meta = {'db_alias': 'transaction'}