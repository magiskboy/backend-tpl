#coding=utf-8

import flask
from flask_cors import CORS     #type:ignore
from flask_boilerplate.model import db
from flask_boilerplate.config import get_config

from .swagger import swagger
from .v1 import v1_bp


def create_app(config_name='production') -> flask.Flask:
    app = flask.Flask(__name__)
    app.config.from_object(get_config(config_name))

    db.init_app(app)
    swagger.init_app(app)
    CORS(app)

    @app.route('/health')
    def health():       #pylint:disable=W0612
        """Check service started
        ---
        responses:
            204:
                description: Service already
        """
        return '', 204

    app.register_blueprint(v1_bp, url_prefix='/v1')

    return app
