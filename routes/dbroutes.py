from config import app,db
from dbmodels import People
from flask import jsonify, request
from utilities import RecordAlreadyExistsError,RecordNotFoundError

@app.route('/api/people',methods=['GET','POST'])
def dbops():
    if request.method=='GET':
        people=People.query.all()
        people=[x.serialize() for x in people]
        #people=[x.serializeordered() for x in people]
        #result= '{ "people":' + str(people) +"}"
        return jsonify({'result':people})
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
        

@app.route('/api/people/<int:sno>',methods=['PUT','PATCH'])
def updatePerson(sno):
    try:
        person=People.query.get(sno)
        if(person):
            input=request.get_json()
            if('name' in input.keys()):
                person.name=input['name']
            if('city' in input.keys()):
                person.city=input['city']
            db.session.commit()
            return jsonify({'status':"success"})
        else:
            raise RecordNotFoundError("No record with sno "+str(sno))
    except RecordNotFoundError as e:
        return {'status':str(e)}, 500
    except:
        print(e)
        return jsonify({'status':"some issue"}), 500