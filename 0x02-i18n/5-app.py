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


app.config.from_object(Config)
users = {
        1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
        2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
        3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
        4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
        }


def get_user(user_id):
    """"
    Get user ID
    """
    return users.get(user_id)


def before_request():
    """
    Before request is set to global variable
    """
    g.user = None
    login_as = request.args.get('login_as')
    if login_as and login_as.isdigit():
        user_id = int(login_as)
        g.user = get_user(user_id)


@babel.localeselector
def get_locale():
    """
    Determining the users preferred language
    """
    if 'locale' in request.args and request.args['locale'] in app.config[
            'LANGUAGES']:
        return request.args['locale']
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """"
    Renders the 4-index.html
    """
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run(debug=True)
