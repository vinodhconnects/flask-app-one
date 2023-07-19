from config import app,db
from dbmodels import People
from flask import jsonify, request

@app.route('/api/people',methods=['GET','POST'])
def dbops():
    if request.method=='GET':
        people=People.query.all()
        print(people)
        return 'success'