#!/usr/bin/env python3
from flask import Flask, render_template, url_for, request
app = Flask(__name__)

@app.route('/')
def index():
    url_for('static', filename='style.css')
    rem = render_template('index.html')
    return rem

@app.route('/login')
def login():
    url_for('static', filename='style.css')
    rem = render_template('login.html')
    return rem

@app.route('/login/dropbox', methods=['POST', 'GET'])
def logdropbox():
    error = None
    url_for('static', filename='style.css')
    rem = render_template('dropbox.html')
    return rem

@app.route('/login/google-drive', methods=['POST', 'GET'])
def loggd():
    error = None
    url_for('static', filename='style.css')
    rem = render_template('google-drive.html')
    return rem

@app.route('/config')
def config():
    url_for('static', filename='style.css')
    rem = render_template('config.html')
    return rem

if __name__ == '__main__':
    app.run(port=9080)

"""
 A guy called "ThiefMaster" in an IRC Channel told me that I can run
 the server from this main script in this way. If you are reading this:
 	I really love you, man.
 Also, another one in the same channel (called "DLSteve") told me how to
 specify the port.
 	I love you too, like bros love.
"""
