from application import db

class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(100), nullable=False)

    def __init__(self, name, email, phone):
        
            self.name = name
            self.email = email
            self.phone = phone
