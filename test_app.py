import unittest
from app import app


class FlaskAppTests(unittest.TestCase):

    def setUp(self):
        app.config["TESTING"] = True
        self.client = app.test_client()

    def test_home_page(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Top University Rankings", response.data)

    def test_stats_page(self):
        response = self.client.get("/stats")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Statistics", response.data)

    def test_404_page(self):
        response = self.client.get("/this-page-does-not-exist")
        self.assertEqual(response.status_code, 404)
        self.assertIn(b"404 - Page Not Found", response.data)

    def test_search_filter(self):
        response = self.client.get("/?search=Oxford")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Top University Rankings", response.data)

    def test_country_filter(self):
        response = self.client.get("/?country=United%20Kingdom")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Top University Rankings", response.data)

    def test_year_filter(self):
        response = self.client.get("/?year=2014")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Top University Rankings", response.data)

    def test_pagination(self):
        response = self.client.get("/?page=2")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Top University Rankings", response.data)

    def test_empty_search(self):
        response = self.client.get("/?search=")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Top University Rankings", response.data)

    def test_detail_page_valid(self):
        response = self.client.get("/university/Harvard University")
        self.assertEqual(response.status_code, 200)

    def test_detail_page_invalid(self):
        response = self.client.get("/university/FakeUniversityXYZ99999")
        self.assertEqual(response.status_code, 404)
        self.assertIn(b"404 - Page Not Found", response.data)


if __name__ == "__main__":
    unittest.main()