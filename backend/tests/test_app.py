import requests

def test_server():
    respon = requests.get('http://localhost:500/')
    assert respon.status_code == 200