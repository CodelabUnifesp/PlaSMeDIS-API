from api.util.decorators import required
from api.service.notifications import GetUserNotification, PutUserNotification
from api import api
from flask_restx import Resource, cors
import api.model.response.notifications as response
import api.model.response.default as default

notifications = api.namespace('notifications', description="Notifications namespace", decorators=[cors.crossdomain(origin="*")])

@notifications.route("/users/<int:id>/conf")
class NotificationConf(Resource):
    @required(response=response.notification_message, token=True)
    def get(self, id):
        return GetUserNotification(id)
    
    @required(response=default.message, request=response.notification, token=True)
    def put(self, data, id):
        return PutUserNotification(data, id)
    