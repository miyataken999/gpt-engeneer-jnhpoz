from flask import Flask, jsonify
from routes.user import user_blueprint

app = Flask(__name__)
app.register_blueprint(user_blueprint)

@app.route('/')
def index():
    return 'Welcome to the API!'