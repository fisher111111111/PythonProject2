from enums import Enum

class ConstURL(Enum):
    BASE_URL = "https://api.fast-api.senior-pomidorov.ru"
    CREATE_TOKEN_ENDPOINT = "/api/v1/login/access-token"
    ITEMS_ENDPOINT = "/api/v1/login/access-token"

class ConstHeaders(Enum):
    CONTENT_TYPE = 'application/x-www-form-urlencoded'
    ACCEPT = 'application/json'
