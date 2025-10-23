from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/post_doubts')
def post_doubts():
    return render_template('post_doubts.html')

@app.route('/solve_doubts')
def solve_doubts():
    return render_template('solve_doubts.html')

@app.route('/st_login')
def st_login():
    return render_template('st_login.html')

@app.route('/tr_login')
def tr_login():
    return render_template('tr_login.html')

if __name__ == '__main__':
    app.run(debug=True)
