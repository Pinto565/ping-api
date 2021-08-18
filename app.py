from components import *
from flask import *
import json

app = Flask(__name__)


@app.after_request
def after_request_func(response):
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add('Access-Control-Allow-Headers', "*")
    response.headers.add('Access-Control-Allow-Methods', "*")
    return response


@app.route("/")
def api():
    update_status()
    return jsonify(status)


if __name__ == "__main__":
    app.run(debug=True)
