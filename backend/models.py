from database import db

class Property(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    location = db.Column(db.String(100))
    price = db.Column(db.String(50))
    image = db.Column(db.String(200))
