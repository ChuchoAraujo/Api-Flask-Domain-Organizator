from models.db import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    username = db.Column(db.String(150), unique=True, nullable=False)
    post = db.relationship('Post', back_populates= 'user')

    def __init__(self, email, password, username):
        self.email = email,
        self.password = password,
        self.username = username
        self.is_active = True

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "username": self.username,
            "active": self.is_active,
            "post": [post.serialize_populate() for post in  self.post]
            
            # do not serialize the password, its a security breach
        }
    def serialize_populate(self):
        return {
            "id": self.id,
            "username": self.username,
        }