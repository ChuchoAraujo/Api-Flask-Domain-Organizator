"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models.index import db, Post, User
from domain.user.route import user_route


#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)



#----------------------------------------------------------------------------------------------------------------------------#
user_route(app)



##RUTAS POST-------------------------

@app.route('/post', methods=['POST'])
def create_post():
    data = request.get_json()
    new_post = Post(title=data['title'], message=data['message'], user_id=data['user_id'])
    db.session.add(new_post)
    db.session.commit()
    return jsonify(new_post.serialize()), 201

@app.route('/post', methods=['GET'])
def get_all_posts():
    all_posts = Post.query.all()
    serialize_posts = [user.serialize() for user in all_posts]
    return jsonify(serialize_posts ), 200


# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
