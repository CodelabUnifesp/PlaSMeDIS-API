import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS

class FlaskApp():
    def __init__(self):
        self.app = Flask(__name__)
        self.cors = CORS(self.app, resources={r"*": {"origins": "*"}})
        self.app.config['CORS_HEADERS'] = 'Content-Type'
        self.app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI', "postgresql://jkpaprazxcpojo:2a135108dda110cdf26d9ef31fff1c6b9f94cd92993f25a90c3df353c685626d@ec2-52-45-179-101.compute-1.amazonaws.com:5432/d5bi00ifg35edj")
        self.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        self.app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', "N5Rc6dvl8giHxExSXQmJ")
        self.db = SQLAlchemy(self.app)
        self.migrate = Migrate(self.app, self.db)

flaskApp = FlaskApp()