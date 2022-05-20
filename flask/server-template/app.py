from distutils.log import debug
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/ping')
def ping():
    """Connection test"""

    print('Looks like something pinging')

    return jsonify('pong')

if __name__ == "__main__":
    print("Backend starting")
    app.run("0.0.0.0", port=5000, debug=debug)