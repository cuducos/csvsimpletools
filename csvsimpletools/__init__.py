from babel import negotiate_locale
from flask import Flask, g, request
from flask_babel import Babel
from flask_wtf.csrf import CSRFProtect

from csvsimpletools.views import main


app = Flask('csvsimpletools')
app.config.from_object('config')
app.register_blueprint(main)

CSRFProtect(app)
babel = Babel(app)


@babel.localeselector
def get_locale():
    locales = app.config.get('LOCALES', {}).keys()
    sent = request.accept_languages.values()
    g.locale = negotiate_locale((v.replace('-', '_') for v in sent), locales)

    if not g.locale:
        g.locale = 'en'

    return g.locale
