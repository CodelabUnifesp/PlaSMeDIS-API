from flask_cors import cross_origin
from api.util.decorators import required
from api.service.notifications import HandleUserNotification
from api import api
from flask_restx import Resource
#import api.model.request.privileges as request
#import api.model.response.privileges as response
import api.model.response.default as default

notifications = api.namespace('notifications', description="Notifications namespace")

@notifications.route("/users/<int:id>/conf")
class NotificationConf(Resource):
    @cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
    @required(response=default.message, token=True)
    def get(self, id):
        return HandleUserNotification(id)
    
    def put(self, id):
        return HandleUserNotification(id)
    