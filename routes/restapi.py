from config import app,getDataFile
from flask import jsonify

@app.get("/")
def home():
    return "Flask is up and running"

@app.get("/greet/<string:name>")
def greet(name):
    return "Hello!!!"+name

@app.get("/filelines")
def filelines():
    lines=[]
    file=getDataFile()
    for x in file.readlines():
        lines.append(x)
    return jsonify({'data':lines})