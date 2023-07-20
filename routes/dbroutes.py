from config import app,db
from dbmodels import People
from flask import jsonify, request

@app.route('/api/people',methods=['GET','POST'])
def dbops():
    if request.method=='GET':
        people=People.query.all()
        people=[x.serializeordered() for x in people]
        result= '{ "people":' + str(people) +"}"
        return result
    if request.method=='POST':
        input=request.get_json()
        person=People(sno=input['sno'],name=input['name'],city=input['city'])
        try:
            db.session.add(person)
            db.session.commit()
            return jsonify({'status': "success"}), 201
        except Exception as e:
            print(e)
            print(str(e.__class__))
            if(str(e.__class__)=="<class 'sqlalchemy.exc.IntegrityError'>"):
                return jsonify({'status':"Primary key already exists"}), 500
            
            return  jsonify({'status':"unsuccessful"}), 500
