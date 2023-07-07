import json # new

import pytest
from starlette.testclient import TestClient

from web_app.main import app


@pytest.fixture
def client():
    return TestClient(app)


def test_health_check(client):
    """
    GIVEN
    WHEN health check endpoint is called with GET method
    THEN response with status 200 and body OK is returned
    """
    response = client.get("/health-check/")
    assert response.status_code == 200
    assert response.data.decode() == "OK"
    
# new
def test_request_talk(client):
    """
    GIVEN event time, address, topic, duration in minutes,
    requester
    WHEN request talk endpoint is called
    THEN request talk with the same attributes as provided is
    returned
    """
    response = client.post(
        "/request-talk/",
        json={
        "event_time": "2021-10-03T10:30:00",
        "address": {
            "street": "Sunny street 42",
            "city": "Sunny city 42000",
            "state": "Sunny state",
            "country": "Sunny country",
        },
        "topic": "FastAPI with Pydantic",
        "duration_in_minutes": 45,
        "requester": "john@doe.com",
        },
    )
    assert response.status_code == 201
    response_body = response.json()
    assert isinstance(response_body["id"], str)
    assert response_body["event_time"] == "2021-10-03T10:30:00"
    assert response_body["address"] == {
    "street": "Sunny street 42",
    "city": "Sunny city 42000",
    "state": "Sunny state",
    "country": "Sunny country",
    }
    assert response_body["topic"] == "FastAPI with Pydantic"
    assert response_body["status"] == "PENDING"
    assert response_body["duration_in_minutes"] == 45
    assert response_body["requester"] == "john@doe.com"
    
     