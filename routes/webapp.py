from config import app,db
from flask import render_template
from dbmodels import People


@app.get("/webapp/")
def uihome():
    return render_template('index.html', programmer="John")

@app.route("/webapp/people",methods=["GET","POST"])
def dbpeopleui():
    """if request.method=="POST":
        sno=request.form['sno']
        name=request.form['name']
        city=request.form['city']
        person=People(sno=sno,name=name,city=city)
        db.session.add(person)
        db.session.commit()"""
    peoplelist=People.query.all()
    return render_template('people.html', plist = peoplelist)
