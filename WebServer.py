from twisted.web import server
from twisted.web.resource import Resource
from twisted.internet import reactor

from resources.TwistedResources import Template1, Bar

print("[Running]")

# TODO put on server
root = Resource()
root.putChild(b"test", Template1())
root.putChild(b"bar", Bar())
site = server.Site(root)
reactor.listenTCP(80, site)
reactor.run()
