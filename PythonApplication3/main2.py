from flask import url_for,Flask,render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', name='Jerry')