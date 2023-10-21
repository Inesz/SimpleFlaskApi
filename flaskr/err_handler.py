from werkzeug.exceptions import HTTPException

from flask import jsonify


class BasicErrStructure():
    code: int
    msg: str

    def __init__(self, code, str):
        self.code = code
        self.str = str


def default_err_handler(e: Exception):
    return jsonify(BasicErrStructure(str(e), 500)), 500


def default_werkzeug_handler(e: HTTPException):
    return jsonify(BasicErrStructure(e.description, e.code).__dict__), e.code
