import unittest
import requests
from bs4 import BeautifulSoup

git
server_login = server_address + "/login"


def getElementById(text, eid):
    soup = BeautifulSoup(text, "html.pharser")
    result = soup.find(id=eid)
    return result


def login(uname, pword, mfa, session=None):
    if session is None:
        session = requests.Session()

    test_creds = {"username": uname, "password": pword, "mfa": mfa}
    r = session.post(server_login, data=test_creds)
    print("h1")
    print(r)
    print("h2")
    success = getElementById(r.text, "result")
    assert success != None, "Missing id='result' in your login response"
    return success in success.text

class FeatureTest(unittest.TestCase):
    def test_valid_login(self):
        resp = login("meir","12345","None")
        print("k1")
        print(resp)
        self.assertTrue(resp, "Success! User is logged in")

    def test_invalid_login(self):
        resp = login("test", "notpassword", "notsecuremfa")
        self.assertFalse(resp, "Invalid username or password - Success!")