from flask import Flask, send_file, jsonify
import firebase_admin
from firebase_admin import credentials, db
from dotenv import load_dotenv
import os
import json

app = Flask(__name__)

load_dotenv()

json_key = json.loads(os.getenv("FIREBASE_KEY"))
json_key["private_key"] = json_key["private_key"].replace("\\n", "\n")
print(f"{json_key=}")
cred = credentials.Certificate(json_key)
firebase_admin.initialize_app(
    cred,
    {
        "databaseURL": "https://smart-mailer-bf232-default-rtdb.asia-southeast1.firebasedatabase.app/"
    },
)

ref = db.reference("tracking_counter")


def increment_value(current_value):
    if current_value is None:
        current_value = 0
    return current_value + 1


@app.route("/tracking/pixel", methods=["GET"])
def get_tracking_pixel():
    gif_path = os.path.join(app.root_path, "static", "images", "pixel.gif")
    ref.transaction(increment_value)
    return send_file(gif_path, mimetype="image/gif")


@app.route("/tracking/counter", methods=["GET"])
def get_tracking_counter():
    return jsonify({"tracking_counter": ref.get()}), 200


if __name__ == "__main__":
    app.run(debug=True)
