from flask import request, jsonify
from models.index import db, User
import domain.user.controller as Controller 

#SOLID -OBJ -FUNC
# 1 SOLA RESPONSABILIDAD


def user_route(app):

    @app.route('/user', methods=['GET'])
    def get_all_users():
        all_users = User.query.all()
        serialize_users = [user.serialize() for user in all_users]
        return jsonify(serialize_users ), 200


    @app.route('/user/<int:id>', methods= ['GET'])
    def get_user(id):
        print(id)
        user = User.query.get(id)
        return jsonify(user.serialize()), 200


    @app.route('/user', methods=['POST'])
    def create_user():
        body = request.get_json()
        data, status = Controller.create_user(body)
        return jsonify(data, status), 200