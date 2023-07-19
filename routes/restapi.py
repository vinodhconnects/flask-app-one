from config import app

@app.get("/")
def home():
    return "Flask is up and running"

@app.get("/greet/<string:name>")
def greet(name):
    return "Hello!!!"+name