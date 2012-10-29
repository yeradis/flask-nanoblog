# flask-nanoblog

## Nanoblogging python-webapp

Just a bored afternoon, pushed me to play with Flask Python web-framework and MongoEngine.

* MongoEngine = The object-document mapper to connect Python and MongoDB

* Flask = A microframework for Python based on Werkzeug, Jinja 2 and good intentions


This can be considered a Fork of http://docs.mongodb.org/manual/tutorial/write-a-tumblelog-application-with-flask-mongoengine/

There is all what you need to do something with more value.

I'd just did my version, a nano one!

btw, to run this nanoblog, there are three ways:

* `server.py`  : run flask apps using flask-script features like running a development server, auto-reload is nice :3
* `server-tornado.py`  : run flask app under tornado through wsgi
* `server-twisted.py`  : run flask app under twisted through wsgi

### installation

I will no go into details, but if you are here is because you have Python installed, so lets continue.

1. Install MongoDB
2. install pip
3. install nanoblog dependencies: `pip install  -r requirements.txt`

Try nanoblog:

    python server.py runserver

Now point your browser to http://localhost:5000

Voila!