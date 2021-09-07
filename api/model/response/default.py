from api import api
from flask_restx import fields

message = api.model("Message",{
    "message": fields.String()
})

success_message = api.model("Success Message", {
    "success": fields.Boolean(),
    "message": fields.String()
})