from django.test import TestCase


class HomePageTest(TestCase):
    def test_home_page(self):
        response = self.client.get('/')
        self.assertIn(
            '<title>To-Do Lists</title>',
            response.content.decode()
        )
        self.assertTrue(response.content.decode().startswith('<html>'))
        self.assertTrue(response.content.decode().endswith('</html>'))
