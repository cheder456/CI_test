import unittest
import requests

class TestAPI(unittest.TestCase):
    URL = "http://127.0.0.1:5000/"

    def test_hello_world(self):

        resp = requests.get(self.URL)
        self.assertEquals(resp.status_code, 200)
