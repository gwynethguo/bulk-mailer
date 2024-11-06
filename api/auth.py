import base64
from functools import wraps
from flask import jsonify, request
import os


def validate_app_key(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        headers = request.headers
        if "Authorization" not in headers:
            return jsonify({"error": "Missing authentication credentials"}), 401

        token = headers.get("Authorization").split()[1]

        if token != os.environ.get("APP_KEY"):
            return jsonify({"error": "Incorrect authentication credentials"}), 401
        else:
            return f(*args, **kwargs)

    return decorated_function


def validate_app_key_req_params(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        params = request.args
        if "app" not in params:
            return jsonify({"error": "Missing authentication credentials"}), 401

        token = params.get("app")
        print(decode_key(token))
        print(os.environ.get("APP_KEY"))
        if decode_key(token) != os.environ.get("APP_KEY"):
            return jsonify({"error": "Incorrect authentication credentials"}), 401
        else:
            return f(*args, **kwargs)

    return decorated_function


def decode_key(encoded_key):
    return base64.b64decode(encoded_key).decode()
