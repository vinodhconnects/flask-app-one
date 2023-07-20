from flask import Flask,send_from_directory
from flask_sqlalchemy import SQLAlchemy
import os

app=Flask(__name__,template_folder="../templates") # Flask object that manages entire application

basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
print(os.path.join(basedir, 'database.db'))
db = SQLAlchemy(app)

def getDataFile(mode):
    return open("staticdata.txt",mode)

#http://localhost:5000/files/resources/x.txt
@app.route("/files/<path:path>")
def get_file(path):
    return send_from_directory('../static',path)