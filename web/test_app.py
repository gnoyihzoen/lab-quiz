import requests

def test_homepage():
    r = requests.get("http://localhost:5000")
    assert r.status_code == 200

def test_valid_password():
    r = requests.post("http://localhost:5000", data={"password": "D$3g8r!qZb"}, allow_redirects=True)
    assert "Welcome" in r.text
