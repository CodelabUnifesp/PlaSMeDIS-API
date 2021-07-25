import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI', "postgresql://jkpaprazxcpojo:2a135108dda110cdf26d9ef31fff1c6b9f94cd92993f25a90c3df353c685626d@ec2-52-45-179-101.compute-1.amazonaws.com:5432/d5bi00ifg35edj")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', "N5Rc6dvl8giHxExSXQmJ")
db = SQLAlchemy(app)
migrate = Migrate(app, db)