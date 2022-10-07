import unittest
import json

from app import create_app


class EventlistTest(unittest.TestCase):

    def setUp(self):
        app = create_app()
        self.app = app.test_client()

    def test_post_happy_path(self):
        # Given
        payload = json.dumps(
            {"filename": "sample1.txt",
             "from": "2000-01-01T17:25:49Z",
             "to": "2000-01-10T16:55:01Z"
             }
        )

        # When
        response = self.app.post(
            '/', headers={"Content-Type": "application/json"}, data=payload)

        # Then
        self.assertEqual(200, response.status_code)

    def test_bad_request(self):
        # Given
        payload = json.dumps(
            {
                "from": "2000-01-01T17:25:49Z",
                "to": "2000-01-10T16:55:01Z"
            }
        )

        # When
        response = self.app.post(
            '/', headers={"Content-Type": "application/json"}, data=payload)

        # Then
        self.assertEqual(200, response.status_code)
        self.assertEqual(list, type(response.json))
        self.assertEqual([], response.json)

    def test_reponse_data(self):
        # Given
        payload = json.dumps(
            {"filename": "sample1.txt",
             "from": "2000-01-01T17:25:49Z",
             "to": "2000-01-10T16:55:01Z"
             }
        )
        # When
        response = self.app.post(
            '/', headers={"Content-Type": "application/json"}, data=payload)

        # Then
        self.assertEqual(200, response.status_code)
        self.assertEqual(list, type(response.json))
        # assert order and length of response
        self.assertEqual(18, len(response.json))
        self.assertGreater(
            response.json[1]['eventTime'], response.json[0]['eventTime'])
