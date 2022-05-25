from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///storage.db'
db = SQLAlchemy(app)


#import precisa ser declarado depois da variavel app ser declarado 
from app.controllers import default