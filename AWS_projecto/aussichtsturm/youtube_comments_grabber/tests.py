import unittest
from django.test import Client

class SimpleTest(unittest.TestCase):
    def setUp(self):
        # Every test needs a client.
        self.client = Client(SERVER_NAME='localhost')

    def test_status(self):
        # Issue a GET request.
        response = self.client.get('/comments/')

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)


