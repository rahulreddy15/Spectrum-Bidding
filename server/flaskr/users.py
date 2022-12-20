from flask import Blueprint, request, make_response, jsonify

from flaskr.db import db_session
from flaskr.models import User, Group

bp = Blueprint('users', __name__, url_prefix='/users')


@bp.route('/getallusers', methods=('GET', 'POST'))
def getallusers():
    if request.method == 'GET':
        try:
            result = User.query.all()
            users = []
            for user in result:
                if not user.admin:
                    users.append(
                        {"username": user.username, "email": user.email, "password": user.password})
            responseObject = {
                'status': 'success',
                'data': users,
            }
            return make_response(jsonify(responseObject)), 201
        except Exception as e:
            print(e)
            responseObject = {
                'status': 'fail',
                'message': 'Some error occurred. Please try again.'
            }
            return make_response(jsonify(responseObject)), 401

def getalladmins():
    if request.method == 'GET':
        try:
            result = User.query.all()
            admins = []
            for user in result:
                if user.admin:
                    admins.append(
                        {"username": user.username, "email": user.email, "password": user.password})
            responseObject = {
                'status': 'success',
                'data': admins,
            }
            return make_response(jsonify(responseObject)), 201
        except Exception as e:
            responseObject = {
                'status': 'fail',
                'message': 'Some error occurred. Please try again.'
            }
            return make_response(jsonify(responseObject)), 401


@bp.route('/updateuser', methods=('GET', 'POST'))
def updateuser():
    pass


@bp.route('/creategroup', methods=('GET', 'POST'))
def creategroup():
    pass
