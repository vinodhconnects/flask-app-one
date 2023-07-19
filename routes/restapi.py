from config import app

@app.get("/")
def home():
    return "Flask is up and running"