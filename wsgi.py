import eventlet
from eventlet import wsgi
from web import app

app = app
wsgi.server(eventlet.listen(("127.0.0.1", 8000)), app)