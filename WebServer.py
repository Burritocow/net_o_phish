from twisted.web import server
from twisted.web.resource import Resource
from twisted.internet import reactor

from resources.TwistedResources import Scholarships, Bar

import logging

logging.basicConfig(filename="out/requests.log", level=logging.INFO)

print("[Running]")

root = Resource()
root.putChild(b"scholarships", Scholarships())
root.putChild(b"bar", Bar())
site = server.Site(root)
reactor.listenTCP(80, site)
reactor.run()
