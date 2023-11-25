import eventlet
from eventlet import wsgi
from web import app

app = app
wsgi.server(eventlet.listen(("", 8000)), app)