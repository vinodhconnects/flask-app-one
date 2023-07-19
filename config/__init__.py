from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app=Flask(__name__) # Flask object that manages entire application

basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

def getDataFile(mode):
    return open("staticdata.txt",mode)