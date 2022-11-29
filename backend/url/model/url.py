from ..database.db import db

class Url(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(150), unique=True)
    short_url = db.Column(db.String(150), unique=True)
    clicks = db.Column(db.Integer, default=0)

