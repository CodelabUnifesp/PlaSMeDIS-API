from api.util.decorators import required
from api import api
from flask_restx import fields

notification = api.model("Notification",
{
    "sistema": fields.Boolean,
    "selo_postagem": fields.Boolean,
    "comentario_postagem": fields.Boolean,
    "saude": fields.Boolean,
    "lazer": fields.Boolean,
    "trocas": fields.Boolean
})

notification_message = api.model("Notification Message", {
    "message": fields.String(),
    "user_not": fields.Nested(notification)
})