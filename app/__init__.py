from flask import Flask

app = Flask(__name__)

#import precisa ser declarado depois da variavel app ser declarado 
from app.controllers import default