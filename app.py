from components import *
from flask import *
import json

app = Flask(__name__)


@app.route("/")
def api():
    update_status()
    return jsonify(status)


if __name__ == "__main__":
    app.run(debug=True)