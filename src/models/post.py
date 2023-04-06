from models.db import db

class Post(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    title = db.Column(db.String(80), nullable=False)
    message =  db.Column(db.String(180), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', back_populates= 'post')

    def __init__(self, title, message, user_id):
        self.title = title,
        self.message = message,
        self.user_id = user_id

    def serialize(self):
        return {
            "id": self.id,
            "title": self.title,
            "message": self.message,
            "user_id": self.user_id,
            "user": self.user.serialize_populate()
        }
    
    def serialize_populate(self):
        return {
            "id": self.id,
            "title": self.title,
            "message": self.message,
        }