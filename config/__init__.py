from flask import Flask

app=Flask(__name__) # Flask object that manages entire application

def getDataFile(mode):
    return open("staticdata.txt",mode)