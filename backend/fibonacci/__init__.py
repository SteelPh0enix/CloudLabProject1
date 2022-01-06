from flask import Flask
from flask_cors import CORS
from . import database

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    CORS(app)
    
    app.config.from_mapping(
        SECRET_KEY='This is my secret key, not so secret anymore',
        SQLALCHEMY_DATABASE_URI='mysql+pymysql://fibonacci:fibo_mysql_password@database/fibonacci',
        SQLALCHEMY_TRACK_MODIFICATIONS=False
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    app.app_context().push()
    database.init_db(app)
    database.db.create_all()

    from . import calculator, history
    app.register_blueprint(calculator.bp)
    app.register_blueprint(history.bp)

    return app