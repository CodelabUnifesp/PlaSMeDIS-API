import os
from flask_cors import cross_origin
from api import app
from api.controller import users, auth, forms, notifications, comments, posts, privileges

app.register_blueprint(users.app)
app.register_blueprint(forms.app)
app.register_blueprint(notifications.app)
app.register_blueprint(comments.app)
app.register_blueprint(posts.app)


# TODO: Mover para controller
@app.route('/')
@cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
def hello():
    return "This API Works! [" + os.environ.get("ENV", "DEV") + "]"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000)
