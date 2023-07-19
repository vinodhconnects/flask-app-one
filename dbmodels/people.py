from config import db

class People(db.Model):
    sno=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.Integer,nullable=False)
    city=db.Column(db.Integer,nullable=False)
   
    def __repr__(self):
        return str(
            {
                'sno': self.sno,
                'name': self.name,
                'city': self.city
            }
        )