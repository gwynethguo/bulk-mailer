from flask import Flask, send_file

app = Flask(__name__)


@app.route("/pixel")
def tracking_pixel():
    return send_file("static/images/pixel.gif", mimetype="image/gif")
