from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_pymongo import PyMongo
from bson.json_util import dumps
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

app = Flask(__name__)

# MongoDB configuration using .env for security
app.config["MONGO_URI"] = os.getenv("MONGO_URI")

# Initialize PyMongo
mongo = PyMongo(app)
db = mongo.db  # Shortcut to access the database

# ------------------- ROUTES -------------------

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # Get form data
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')

        # Insert into MongoDB 'users' collection
        db.users.insert_one({
            'name': name,
            'email': email,
            'password': password  # Later hash this for security
        })
        return redirect(url_for('st_login'))
    return render_template('signup.html')

@app.route('/st_login', methods=['GET', 'POST'])
def st_login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = db.users.find_one({'email': email, 'password': password})
        if user:
            return redirect(url_for('post_doubts'))
        else:
            return "Invalid login credentials", 401
    return render_template('st_login.html')

@app.route('/tr_login')
def tr_login():
    return render_template('tr_login.html')

@app.route('/post_doubts', methods=['GET', 'POST'])
def post_doubts():
    if request.method == 'POST':
        question = request.form.get('question')
        subject = request.form.get('subject')

        db.doubts.insert_one({
            'question': question,
            'subject': subject
        })
        return jsonify({'message': 'Doubt posted successfully!'})
    return render_template('post_doubts.html')

@app.route('/solve_doubts')
def solve_doubts():
    doubts = list(db.doubts.find({}, {'_id': 0}))
    return render_template('solve_doubts.html', doubts=doubts)

# ------------------------------------------------

if __name__ == '__main__':
    app.run(debug=True)
