from flask import Flask

app=Flask(__name__) # Flask object that manages entire application

def getDataFile():
    return open("staticdata.txt","r")