# Set the path
import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from nanoblog import app

# run in under twisted through wsgi
from twisted.internet import reactor
from twisted.web.server import Site
from twisted.web.wsgi import WSGIResource

resource = WSGIResource(reactor, reactor.getThreadPool(), app)
site = Site(resource)

reactor.listenTCP(5000, site, interface="0.0.0.0")
reactor.run()