from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    notes = db.relationship('Note')
 
     
class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    manual_date = db.Column(db.String(20))
    body_parts = db.Column(db.String(100))
    exercise_name = db.Column(db.String(10000))
    num_of_sets = db.Column(db.Integer)
    num_of_reps = db.Column(db.Integer)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))