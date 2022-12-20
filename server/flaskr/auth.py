import functools
import datetime
from flask import Blueprint, request, make_response, jsonify

from flaskr.db import db_session
from flaskr.models import User

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        
        data = request.get_json()
        print(data.get('admin'))
        user = User.query.filter_by(email=data.get('email')).first()
        if not user:
            try:
                user = User(data.get('username'), data.get('email'), data.get('password'), datetime.datetime.now(), data.get('admin'))
                db_session.add(user)
                db_session.commit()

                responseObject = {
                    'status': 'success',
                    'message': 'Successfully registered.',
                }
                return make_response(jsonify(responseObject)), 201
            except Exception as e:
                responseObject = {
                    'status': 'fail',
                    'message': 'Some error occurred. Please try again.'
                }
                return make_response(jsonify(responseObject)), 401
        else:
            responseObject = {
                'status': 'fail',
                'message': 'User already exists. Please Log in.',
            }
            return make_response(jsonify(responseObject)), 202

@bp.route('/login', methods=('GET', 'POST'))
def login():
    pass
