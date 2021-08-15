from components import *
from flask import *

app = Flask(__name__)

@app.route("/")
def index():
    update_status()
    return jsonify(status)

if __name__ == "__main__":
    app.run(debug=True)