from flask import Flask, send_file
import os

app = Flask(__name__)


@app.route("/pixel")
def tracking_pixel():
    gif_path = os.path.join(app.root_path, "static", "images", "pixel.gif")
    return send_file(gif_path, mimetype="image/gif")


if __name__ == "__main__":
    app.run(debug=True)
