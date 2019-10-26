import unittest
import requests

server_address = "http://127.0.0.1:5000"

class FeatureTest(unittest.TestCase):
    def test_server_is_alive(self):
        req = requests.get(server_address)
        self.assertEqual(req.status_code, 200)

    def test_login_page_exsits(self):
        req = requests.get(server_address + "/login")
        self.assertEqual(req.status_code, 200)

    def test_page_exsits(self):
        pages = ["", "/register", "/login", "/spell_check"]
        for page in pages:
            req = requests.get(server_address + page)
            self.assertEqual((req.status_code, 200))