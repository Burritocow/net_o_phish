from twisted.web.resource import Resource
from resources.DAO import Hook
from MySqlConnection import session

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


class Template1(Resource):
    def render_GET(self, request):
        dict = decode_request_args(request.args)
        request.responseHeaders.addRawHeader("Content-Type", "text/html; charset=utf-8")
        uid = dict.get("uid")[0]

        hook = Hook(uid=uid, template=2)
        session.add(hook)
        session.commit()
        # TODO create and append to a logger file
        return "<html>uid: {}</html>".format(uid).encode("utf-8")


class Bar(Resource):
    isLeaf = True
    def render_GET(self, request):
        request.responseHeaders.addRawHeader("Content-Type", "text/html; charset=utf-8")
        return "<html>Bar!</html>".encode("utf-8")