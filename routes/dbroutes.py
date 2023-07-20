from config import app,db
from dbmodels import People
from flask import jsonify, request

@app.route('/api/people',methods=['GET','POST'])
def dbops():
    if request.method=='GET':
        people=People.query.all()
        people=[x.serialize() for x in people]
        return jsonify({'people': people})
    if request.method=='POST':
        input=request.get_json()
        person=People(sno=input['sno'],name=input['name'],city=input['city'])
        try:
            db.session.add(person)
            db.session.commit
            return jsonify({'status': "success"}), 201
        except:
            return jsonify({'status':"unsuccessful"}), 500
