from config import app
from flask import render_template


@app.get("/webapp/")
def uihome():
    return render_template('index.html', programmer="John")

