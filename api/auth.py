import base64
from functools import wraps
from flask import jsonify, request
import os


def validate_app_key(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        headers = request.headers

        # Check if the Authorization header is present
        if "Authorization" not in headers:
            return jsonify({"error": "Missing authentication credentials"}), 401

        # Extract the token from the Authorization header
        try:
            token = headers.get("Authorization").split()[1]
        except IndexError:
            return jsonify({"error": "Invalid token format"}), 401

        # Validate the token against the environment variable
        if token != os.environ.get("APP_KEY"):
            return jsonify({"error": "Invalid authentication credentials"}), 401

        return f(*args, **kwargs)

    return decorated_function


def validate_app_key_req_params(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        params = request.args

        # Check if the 'app' parameter is present in the request arguments
        if "app" not in params:
            return jsonify({"error": "Missing authentication credentials"}), 401

        # Extract the token from the 'app' parameter
        token = params.get("app")

        # Decode and validate the token against the environment variable
        if decode_key(token) != os.environ.get("APP_KEY"):
            return jsonify({"error": "Incorrect authentication credentials"}), 401

        return f(*args, **kwargs)

    return decorated_function


def decode_key(encoded_key):
    """
    Decode a base64 encoded key.

    :param encoded_key: The base64 encoded key to decode.
    :return: The decoded key as a string.
    """
    return base64.b64decode(encoded_key).decode()
