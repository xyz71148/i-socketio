import json
import unittest
import coverage

cov = coverage.coverage(branch=True)
cov.start()

from flask import Flask, session, request, json as flask_json
from flask_socketio import SocketIO, send, emit, join_room, leave_room, \
    Namespace, disconnect

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
socketio = SocketIO(app)
disconnected = None


@socketio.on('connect')
def on_connect():
    if request.args.get('fail'):
        return False
    send('connected')
    send(json.dumps(request.args.to_dict(flat=False)))
    send(json.dumps({h: request.headers[h] for h in request.headers.keys()
                     if h not in ['Host', 'Content-Type', 'Content-Length']}))


@socketio.on('disconnect')
def on_disconnect():
    global disconnected
    disconnected = '/'


@socketio.on('connect', namespace='/test')
def on_connect_test():
    send('connected-test')
    send(json.dumps(request.args.to_dict(flat=False)))
    send(json.dumps({h: request.headers[h] for h in request.headers.keys()
                     if h not in ['Host', 'Content-Type', 'Content-Length']}))


@socketio.on('disconnect', namespace='/test')
def on_disconnect_test():
    global disconnected
    disconnected = '/test'


@socketio.on('message')
def on_message(message):
    send(message)
    if message == 'test session':
        session['a'] = 'b'
    if message not in "test noackargs":
        return message


@socketio.on('json')
def on_json(data):
    send(data, json=True, broadcast=True)
    if not data.get('noackargs'):
        return data


@socketio.on('message', namespace='/test')
def on_message_test(message):
    send(message)


@socketio.on('json', namespace='/test')
def on_json_test(data):
    send(data, json=True, namespace='/test')


@socketio.on('my custom event')
def on_custom_event(data):
    emit('my custom response', data)
    if not data.get('noackargs'):
        return data


@socketio.on('other custom event')
@socketio.on('and another custom event')
def get_request_event(data):
    global request_event_data
    request_event_data = request.event
    emit('my custom response', data)


def get_request_event2(data):
    global request_event_data
    request_event_data = request.event
    emit('my custom response', data)

socketio.on_event('yet another custom event', get_request_event2)


@socketio.on('my custom namespace event', namespace='/test')
def on_custom_event_test(data):
    emit('my custom namespace response', data, namespace='/test')


def on_custom_event_test2(data):
    emit('my custom namespace response', data, namespace='/test')

socketio.on_event('yet another custom namespace event', on_custom_event_test2,
                  namespace='/test')


@socketio.on('my custom broadcast event')
def on_custom_event_broadcast(data):
    emit('my custom response', data, broadcast=True)


@socketio.on('my custom broadcast namespace event', namespace='/test')
def on_custom_event_broadcast_test(data):
    emit('my custom namespace response', data, namespace='/test',
         broadcast=True)


@socketio.on('join room')
def on_join_room(data):
    join_room(data['room'])


@socketio.on('leave room')
def on_leave_room(data):
    leave_room(data['room'])


@socketio.on('join room', namespace='/test')
def on_join_room_namespace(data):
    join_room(data['room'])


@socketio.on('leave room', namespace='/test')
def on_leave_room_namespace(data):
    leave_room(data['room'])


@socketio.on('my room event')
def on_room_event(data):
    room = data.pop('room')
    emit('my room response', data, room=room)


@socketio.on('my room namespace event', namespace='/test')
def on_room_namespace_event(data):
    room = data.pop('room')
    send('room message', room=room)


@socketio.on_error()
def error_handler(value):
    if isinstance(value, AssertionError):
        global error_testing
        error_testing = True
    else:
        raise value
    return value


@socketio.on('error testing')
def raise_error(data):
    raise AssertionError()


@socketio.on_error('/test')
def error_handler_namespace(value):
    if isinstance(value, AssertionError):
        global error_testing_namespace
        error_testing_namespace = True
    else:
        raise value
    return value


@socketio.on("error testing", namespace='/test')
def raise_error_namespace(data):
    raise AssertionError()


@socketio.on_error_default
def error_handler_default(value):
    if isinstance(value, AssertionError):
        global error_testing_default
        error_testing_default = True
    else:
        raise value
    return value


@socketio.on("error testing", namespace='/unused_namespace')
def raise_error_default(data):
    raise AssertionError()


class MyNamespace(Namespace):
    def on_connect(self):
        send('connected-ns')
        send(json.dumps(request.args.to_dict(flat=False)))
        send(json.dumps(
            {h: request.headers[h] for h in request.headers.keys()
             if h not in ['Host', 'Content-Type', 'Content-Length']}))

    def on_disconnect(self):
        global disconnected
        disconnected = '/ns'

    def on_message(self, message):
        send(message)
        if message == 'test session':
            session['a'] = 'b'
        if message not in "test noackargs":
            return message

    def on_json(self, data):
        send(data, json=True, broadcast=True)
        if not data.get('noackargs'):
            return data

    def on_exit(self, data):
        disconnect()

    def on_my_custom_event(self, data):
        emit('my custom response', data)
        if not data.get('noackargs'):
            return data

    def on_other_custom_event(self, data):
        global request_event_data
        request_event_data = request.event
        emit('my custom response', data)


socketio.on_namespace(MyNamespace('/ns'))


@app.route('/session')
def session_route():
    session['foo'] = 'bar'
    return ''


class TestSocketIO(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass


    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_connect(self):
        self.assertFalse(False)

if __name__ == '__main__':
    unittest.main()
