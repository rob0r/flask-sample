from flask import Blueprint, render_template, flash
from flask_nav import Nav
from flask_nav.elements import Navbar, View, Subgroup, Link, Text, Separator

# create frontend blueprint for use by the app
frontend = Blueprint('frontend', __name__)

# flask-navbar
# ============================================================================
nav = Nav()
nav.register_element('frontend_top', Navbar(  
    View('Demo app', '.index'),
    View('flash!', '.exampleflash'),
    Subgroup(
        'links',
        Link('python', 'https://www.python.org/'),
        Separator(),
        Link('flask', 'http://flask.pocoo.org/'),
        Link('flask-bootstrap', 'https://pythonhosted.org/Flask-Bootstrap/'),
        Link('flask-nav', 'http://pythonhosted.org/Flask-Bootstrap/nav.html'),
        Link('flask-wtf', 'http://flask-wtf.readthedocs.io/en/latest/'),
    ),
))

# routes
# ============================================================================
@frontend.route('/')
def index():
    from flask_bootstrap import __version__ as FLASK_BOOTSTRAP_VERSION
    from platform import version as platform_version
    from sys import version as sys_version
    version_info = {
        'flask_bootstrap_version' : FLASK_BOOTSTRAP_VERSION,
        'platform_version' : platform_version(),
        'sys_version' : sys_version.replace('[', '').replace(']', '')
    }
    return render_template('index.html', version_info=version_info)

@frontend.route('/exampleflash')
def exampleflash():
    flash('Delivered via the frontend')
    return render_template('flashmessage.html')