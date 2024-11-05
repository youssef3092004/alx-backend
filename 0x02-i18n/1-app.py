from flask import Flask, render_template
from flask_babel import Babel

class Config:
    """
    Config class for Babel
    """
    app = Flask(__name__)
    babel = Babel(app)
    app.config.from_object(Config)

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'

    @app.route('/', strict_slashes=False)
    def index():
        """
        Renders a basic html template
        """
        return render_template('1-index.html')
