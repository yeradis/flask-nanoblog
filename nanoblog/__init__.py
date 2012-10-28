# Flask initializacion stuff

from flask import Flask
app = Flask(__name__)
app.config.from_pyfile('config.py')

#imporing blueprints/views after flask initialization
from nanoblog.views import posts
from nanoblog.admin import admin
#register blue prints so they get available to flask app
app.register_blueprint(posts)
app.register_blueprint(admin)



if __name__ == '__main__':
    app.run()
