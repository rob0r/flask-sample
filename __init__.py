__doc__ = '''
intertoobz
    Author      : Rob / github.com/rob0r
    Description : flask-bootstrap demo app
    Stylesheet  : https://bootswatch.com/slate/

    Usage:
        pip install -r flask_sample/requirements.txt
        export FLASK_DEBUG=1
        export SECRET_KEY=your_super_private_key_here
        flask -app flask_sample
'''

import os
from flask import Flask
from flask_appconfig import AppConfig
from flask_bootstrap import Bootstrap

from .frontend import frontend, nav


def create_app(configfile=None):
    # create flask app
    app = Flask(__name__)

    # add bootstrap to app
    Bootstrap(app)

    # register the frontend blueprint
    app.register_blueprint(frontend)

    app.secret_key = os.environ['secret_key']

    # add nav bar to app
    nav.init_app(app)

    return app