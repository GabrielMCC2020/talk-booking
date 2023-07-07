import requests

def test_health_check():
    response = requests.get("https://development.talkbooking.com/health-check/")

    assert response.status_code == 200
    assert response.json() == {"message": "OK"}

