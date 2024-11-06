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

        print(f"{token=} {os.environ.get("APP_KEY")=}")
        if token != os.environ.get("APP_KEY"):
            return jsonify({"error": "Incorrect authentication credentials"}), 401
        else:
            return f(*args, **kwargs)

    return decorated_function
