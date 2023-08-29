#!/usr/bin/env python3
"""
Basic Flask app with babel localization support
"""
from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config:
    """
    class config  attributes
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


@app.config.from_objects(Config)
def get_locale():
    """
    Determining the users preferred language
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])
@app.route('/')
def index():
    """"
    Renders the 0-index.html
    """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(debug=True)
