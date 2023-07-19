from config import app,getDataFile
from flask import jsonify,request

@app.get("/")
def home():
    return "Flask is up and running"

@app.get("/greet/<string:name>")
def greet(name):
    return "Hello!!!"+name

@app.route("/filelines", methods = ['GET', 'POST'])
def filelines():
    if request.method == 'GET':
        lines=[]
        file=getDataFile('r')
        for x in file.readlines():
            lines.append(x)
        return jsonify({'data':lines})
    if request.method == 'POST':
        input=request.get_json()
        file=getDataFile('a')
        for x in input['data']:
            file.write(x+"\n")
        file.close()
        return 'success'
