Flask-SocketIO
==============

[![Build Status](https://travis-ci.org/xyz71148/i_socketio.png?branch=master)](https://travis-ci.org/xyz71148/i_socketio)

Socket.IO integration for Flask applications.

[预览](https://xyz71148.github.io/i_socketio/index.html)

Installation
------------


You can install this package as usual with pip:

    
    git add . && git commit -m "no msg" && git push origin master && \
    pip3 install git+https://github.com/xyz71148/i-socketio
    
    virtualenv venv
    source venv/bin/activate
    pip install -r requirements.txt
    
    python setup.py register
    python setup.py check
    python setup.py sdist
    python setup.py upload
    python setup.py register sdist upload


Example
-------

```py
from flask import Flask, render_template
from flask_socketio import SocketIO, emit
    
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('my event')
def test_message(message):
    emit('my response', {'data': 'got it!'})

if __name__ == '__main__':
    socketio.run(app)
```

Resources
---------

- [Tutorial](http://blog.miguelgrinberg.com/post/easy-websockets-with-flask-and-gevent)
- [Documentation](http://flask-socketio.readthedocs.io/en/latest/)
- [PyPI](https://pypi.python.org/pypi/Flask-SocketIO)
- [Change Log](https://github.com/xyz71148/i_socketio/blob/master/CHANGES.md)
- Questions? See the [questions](https://stackoverflow.com/questions/tagged/flask-socketio) others have asked on Stack Overflow, or [ask](https://stackoverflow.com/questions/ask?tags=python+flask-socketio+python-socketio) your own question.

