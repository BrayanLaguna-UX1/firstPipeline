import requests

def test_server():
    respon = requests.get('http://localhost:5000/')
    assert respon.status_code == 200