from django.test import TestCase


class HomePageTest(TestCase):

    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_handles_post_request(self):
        response = self.client.post('/newitem', {'item_text': 'a list item'})
        self.assertIn('a list item', response.content)
