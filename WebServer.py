from twisted.web import server
from twisted.web.resource import Resource
from twisted.internet import reactor

from resources.TwistedResources import Scholarships, Bar

import logging
import yaml

props = yaml.load(open('config/config.yaml', 'r'))

logging.basicConfig(filename=props["logging"]["logfile"], level=logging.INFO)

print("[Running]")

root = Resource()
root.putChild(b"scholarships", Scholarships())
root.putChild(b"bar", Bar())
site = server.Site(root)
reactor.listenTCP(props["twisted"]["port"], site)
reactor.run()
