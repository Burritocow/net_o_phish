from twisted.web.template import Element, XMLFile
from twisted.python.filepath import FilePath


class ScholarshipPage(Element):
    loader = XMLFile(FilePath('web/xml/scholarshipsTemplate.xml'))