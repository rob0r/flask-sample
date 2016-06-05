# flask-sample
Sample flask app with bootstrap

- [flask](http://flask.pocoo.org/)
- [flask-bootstrap](https://pythonhosted.org/Flask-Bootstrap/)
- [flask-nav](http://pythonhosted.org/Flask-Bootstrap/nav.html)

## run
virtualenv recommended
```
pip install -r flask-sample/requirements.txt
export FLASK_DEBUG=1
export SECRET_KEY=your_super_private_key_here
flask -app flask-sample
```