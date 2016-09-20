#!/usr/bin/env python3
from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route('/')
def index():
    rem = render_template('index.html')
    url_for('static', filename='style.css')
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
