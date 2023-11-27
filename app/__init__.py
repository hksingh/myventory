# Imports from Flask
from flask import Flask, render_template
# Other imports
import os
import config
import re

basedir = os.path.abspath(os.path.dirname(__file__))
app_env = os.environ.get("FLASK_ENV")

if app_env is None:
    app_env = "Development"
    print(app_env)

def create_app(config_env=app_env):
    app = Flask(__name__)

    @app.route("/")
    def home():
        return render_template('home.html')

    @app.route("/test")
    def test():
        return render_template('test.html')
    return app