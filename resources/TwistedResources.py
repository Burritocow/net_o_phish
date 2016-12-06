from twisted.web.resource import Resource
from twisted.web.template import renderElement
from twisted.web.server import NOT_DONE_YET
from resources.DAO import Bite
from MySqlConnection import session
from web.elements.ScholarshipsElements import ScholarshipPage

import datetime, logging


def decode_request_args(dict):
    fixed_dictionary = {}

    for byte_key in dict:
        fixed_key = byte_key.decode()
        byte_sublist = dict.get(byte_key)
        fixed_sublist = []

        for byte_arg in byte_sublist:
            fixed_sublist.append(byte_arg.decode())

        fixed_dictionary[fixed_key] = fixed_sublist

    return fixed_dictionary


class Scholarships(Resource):
    def render_GET(self, request):
        requestRecievedTime = datetime.datetime.now()

        dict = decode_request_args(request.args)
        uid = dict.get("uid")[0]
        template = dict.get("template")[0]

        bite = Bite(uid=uid, template=template, access_time=requestRecievedTime)
        session.add(bite)
        session.commit()

        logging.info("Request received; uid: %s, template: %s, access_time: %s", uid, template,
                     str(requestRecievedTime))

        request.responseHeaders.addRawHeader("Content-Type", "text/html; charset=utf-8")
        renderElement(request, ScholarshipPage())
        return NOT_DONE_YET


class Bar(Resource):
    isLeaf = True

    def render_GET(self, request):
        request.responseHeaders.addRawHeader("Content-Type", "text/html; charset=utf-8")
        renderElement(request, ScholarshipPage())
        return NOT_DONE_YET
