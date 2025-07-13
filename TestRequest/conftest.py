

import pytest
import requests
from requests import session


@pytest.fixture(scope='session')
def session_req():
    return requests.Session()
