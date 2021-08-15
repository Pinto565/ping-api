from components import *
from flask import *

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/status")
def api():
    update_status()
    return jsonify(status)

if __name__ == "__main__":
    app.run(debug=True)