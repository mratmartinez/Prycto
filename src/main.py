from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route('/')
def index():
    rem = render_template('index.html')
    url_for('static', filename='style.css') 
    return rem

