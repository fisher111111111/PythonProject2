
import pytest
import requests

from TestRequest.conftest import session_req


def test_request(session_req):

    # data = {
    # "username": "admin",
    # "password": "password123"
    # }
    #
    # base_url = 'https://restful-booker.herokuapp.com/auth'

    # response = requests.post(url=base_url, json=data)
    # response_json = response.json()
    # response = requests.get(url='https://restful-booker.herokuapp.com/booking').json()
    # print(response)

    # print(response.headers)
    # print(response.status_code)
    # assert response.status_code == 200
    # print(response.cookies)
    # print(response_json)

    # session_req.post(url=base_url, json=data)
    session_req.headers.update({"new_headers": "new_value"})
    print(session_req.headers)