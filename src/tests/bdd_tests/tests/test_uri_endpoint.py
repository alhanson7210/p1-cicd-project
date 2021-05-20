import os
import pytest
import requests
from pytest_bdd import scenarios, when, then

test_uri = os.getenv("TEST")

ENDPOINT_PATH = "http://localhost" if not test_uri else test_uri
FEATURE = "../features/uri_endpoint.feature"
scenarios(FEATURE)

@pytest.fixture
@when('I wish to test the endpoint from the test uri given by the gh action secret')
def test_uri_endpoint():
    params = {'format': 'json'}
    formatted_path = ENDPOINT_PATH
    response = requests.get(formatted_path, params)
    return response

@then('the response status code should be 200')
def test_uri_endpoint_status_code_is_ok(test_uri_endpoint):
    assert test_uri_endpoint.status_code == 200

