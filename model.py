from app import db


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    desc = db.Column(db.String(1000))
    assignto = db.Column(db.String(100))
    asdate = db.Column(db.String(100))
    prior = db.Column(db.String(100))
    complete = db.Column(db.Boolean)
