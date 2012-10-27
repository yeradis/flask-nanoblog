# flask-nanoblog with a Django style ? 
import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask.ext.script import Manager, Server
from nanoblog import app

manager = Manager(app)

# Accept connections from everywhere 0.0.0.0 on port 5000
# but we need to specify the server command 
# to run the flask-script development server
# but for production use as a wsgi with Tornado , Twisted, Nginx or whatever 	
manager.add_command("runserver", Server(
    use_debugger = True,
    use_reloader = True,
    host = '0.0.0.0')
)

if __name__ == "__main__":
    manager.run()
