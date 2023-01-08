from mongoengine import connect
from mongoengine import *
from datetime import datetime
from app import configs
from .management import UserUnitRoles, Users
from .master import BlastStatus
from .master import Platforms
from .transaction import MutationPaymentStatus
from .master import Categories


connect(alias='content', db=configs.mongoDbContent, host=configs.mongoHost, port=configs.mongoPort)

class Segments(Document):
    segmentName = StringField(required=True)
    segmentAge = DictField(null=True)
    segmentClass = ListField(null=True)
    segmentGender = ListField(null=True)
    segmentInterest = ListField(null=True)
    segmentLocation = ListField(null=True)
    createdAt = DateTimeField(required=True, default=datetime.utcnow())
    updatedAt = DateTimeField(required=True, default=datetime.utcnow())
    updatedBy = ReferenceField(UserUnitRoles, null=True)
    createdBy = ReferenceField(UserUnitRoles, null=True)
    isActive = BooleanField(required=True, default=True)
    isDelete = BooleanField(required=True, default=False)

    meta = {'db_alias': 'content'}

class Contents(Document):
    payloadMessage = DictField(required=True)
    contentName = StringField(required=True)
    contentMessage = DictField(required=True)
    contentEstimateTarget = DecimalField(required=True, min_value=0, precision=2)
    contentDuration = IntField(required=True, default=1)
    contentPrice = DecimalField(required=True, min_value=0, precision=2)
    platformId = ReferenceField(Platforms, required=True)
    blastStatusId = ReferenceField(BlastStatus, required=True)
    paymentStatus = ReferenceField(MutationPaymentStatus, required=True)
    segmentId = ReferenceField(Segments, required=True)
    createdAt = DateTimeField(required=True, default=datetime.utcnow())
    updatedAt = DateTimeField(required=True, default=datetime.utcnow())
    reviewedAt = DateTimeField(null=True)
    reviewedBy = ReferenceField(UserUnitRoles, null=True)
    updatedBy = ReferenceField(UserUnitRoles, null=True)
    createdBy = ReferenceField(UserUnitRoles, null=True)
    isReview = BooleanField(required=True, default=False)
    isActive = BooleanField(required=True, default=True)
    isDelete = BooleanField(required=True, default=False)

    meta = {'db_alias': 'content'}
    
class ContentBlastStatus(Document):
    contentId = ReferenceField(Contents, required=True)
    blastStatusId = ReferenceField(BlastStatus, required=True)
    createdAt = DateTimeField(required=True, default=datetime.utcnow())
    updatedAt = DateTimeField(required=True, default=datetime.utcnow())
    updatedBy = ReferenceField(UserUnitRoles, null=True)
    createdBy = ReferenceField(UserUnitRoles, null=True)
    isActive = BooleanField(required=True, default=True)
    isDelete = BooleanField(required=True, default=False)
    

class Templates(Document):
    templateName = StringField(required=True, unique=True) 
    templateCode = StringField(required=True, unique=True) 
    templateContent = StringField(required=True, unique=True) 
    templateLength = IntField(required=True)
    categoryId = ReferenceField(Categories, required=True)
    createdAt = DateTimeField(required=True, default=datetime.utcnow())
    updatedAt = DateTimeField(required=True, default=datetime.utcnow())
    updatedBy = ReferenceField(Users, null=True)
    createdBy = ReferenceField(Users, null=True)
    isActive = BooleanField(required=True, default=True)
    isDelete = BooleanField(required=True, default=False)

    meta = {'db_alias': 'content'}