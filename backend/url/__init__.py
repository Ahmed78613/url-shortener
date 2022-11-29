
from flask import Flask, jsonify
from flask_cors import CORS
from .routes.main import main_route
from .database.db import db
from dotenv import load_dotenv
from os import environ
# Instance of a flask web application
app = Flask(__name__)
#  Register Blueprint (2nd param optional)
app.register_blueprint(main_route)
CORS(app)

# Load Dotenv
load_dotenv()
app.config.update(
    SQLALCHEMY_DATABASE_URI=environ.get('DATABASE_URL'),
    SQLALCHEMY_TRACK_MODIFICATIONS=environ.get('SQLALCHEMY_TRACK_MODIFICATIONS')
)
# Initialize app
with app.app_context():
    db.app = app
    db.init_app(app)

# Pages on our website (With route) 
@app.route("/")
def home():
    msg = {"msg": "Welcome to our api"}
    return jsonify(msg), 200

# Run app
if __name__ == "__main__":
    app.run(debug=True)
