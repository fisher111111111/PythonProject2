from enum import Enum

class ConstHeaders(Enum):
    HEADERS = (("Content-Type","application/json"), ("Accept","application/json"))
    CONTENT_TYPE = 'application/json'
    ACCEPT = 'application/json'

headers_dict = dict(ConstHeaders.HEADERS.value)
