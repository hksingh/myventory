# Imports from Flask
from flask import Flask, render_template
# Other imports
import os
import config
import re

basedir = os.path.abspath(os.path.dirname(__file__))

def create_app():
    app = Flask(__name__)

    @app.route("/")
    def home():
        return render_template('home.html')

    @app.route("/test")
    def test():
        return render_template('test.html')

    return app