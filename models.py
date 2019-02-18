from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Consultants(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    bio = db.Column(db.String(100))
    qualification = db.Column(db.String(100))
    expertise = db.Column(db.String(100))