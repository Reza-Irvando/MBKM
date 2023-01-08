from app import app
from app.controllers import content

app.route ("/content/template/list", methods = ["GET"])(content.TemplateList)
app.route ("/content/template/create", methods = ["POST"])(content.TemplateCreate)
app.route ("/content/template/detail", methods = ["GET"])(content.TemplateDetail)
app.route ("/content/template/update", methods = ["PUT"])(content.TemplateUpdate)
app.route ("/content/template/delete", methods = ["DELETE"])(content.TemplateDelete)

app.route ("/content/list", methods = ["GET"])(content.ContentList)
app.route ("/content/create", methods = ["POST"])(content.ContentCreate)
app.route ("/content/approve", methods = ["PUT"])(content.ContentApprove)
app.route ("/content/reject", methods = ["PUT"])(content.ContentReject)
app.route ("/content/revision", methods = ["PUT"])(content.ContentRevision)