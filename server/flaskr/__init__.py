import os

from flask import Flask

def create_app():
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
    )

    # initialize the database
    from . import db
    db.init_db()

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    from . import users
    app.register_blueprint(users.bp)

    from . import auth
    app.register_blueprint(auth.bp)

    
    # a simple page that says hello
    @app.route('/server_check')
    def hello():
        return 'Server is running'

    return app