import pytest

base_url = 'https://restful-booker.herokuapp.com/'

@pytest.fixture(scope="session")
def baseURL():
    return base_url

@pytest.fixture(scope="session")
def creds():
    return {
        "username": "admin",
        "password": "password123"
    }

@pytest.fixture
def new_booking():
    return {
        "firstname": "Michael",
        "lastname": "Ball",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }

@pytest.fixture
def updated_booking():
    return {
        "firstname": "Michael",
        "lastname": "Ball",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2019-01-01",
            "checkout": "2020-01-01"
        },
        "additionalneeds": "no Breakfast"
    }
