#!/usr/bin/env python3
"""
Basic Flask app with a single route
"""
from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Confing:
    """
    class cinfig attributes
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


@app.config.from_objects(Config)
@app.route('/')
def index():
    """"
    Renders the 0-index.html
    """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run()
