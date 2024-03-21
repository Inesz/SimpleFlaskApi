import logging
import os
from werkzeug.exceptions import HTTPException

from flask import Flask, jsonify, request
from flask_pydantic.exceptions import ValidationError

from flaskr import api_input
from flaskr.api_input import SomeInput, Gender
from flaskr.constants import HttpMethod
from flaskr.err_handler import default_err_handler, default_werkzeug_handler, default_validation_handler
from flask_pydantic import validate

from flaskr.serializable_base_model import SomeOutput


def create_app(test_config=None):
    logging.debug("create and configure the app")
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
        FLASK_PYDANTIC_VALIDATION_ERROR_RAISE=True,
    )
    app.json.sort_keys = False


    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    app.register_error_handler(Exception, default_err_handler)
    app.register_error_handler(HTTPException, default_werkzeug_handler)
    app.register_error_handler(ValidationError, default_validation_handler)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        logging.warning('Can not create default folder app.instance_path: SimpleFlaskApi/instance')

    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    @app.route('/give-serialized/<age>')
    def give_serialized(age):
        out = SomeOutput(name = "abc",
        age = age,
        acceptance = True,
        gender = Gender.F,
        preferences = "yellow")

        return jsonify(out.to_dict())

    @app.route('/tell-me-sth', methods=[HttpMethod.GET.value, HttpMethod.POST.value])
    def tell_me_sth():
        method = request.method
        body = request.data
        resp = "{}"

        if method == HttpMethod.POST:
            resp = jsonify({"i_see": str(body)})
        elif method == HttpMethod.GET:
            resp = jsonify({"are_you_sure": method})

        return resp, 200

    @app.route('/validation', methods=[HttpMethod.POST.value])
    @validate()
    def validation(body: SomeInput):
        return jsonify(body.__dict__), 200

    return app
