from models.index import db, User

def create_user(data):
    new_user = User(email = data['email'], password = data['password'], username = data['username'])
    db.session.add(new_user)
    db.session.commit()
    return new_user.serialize()