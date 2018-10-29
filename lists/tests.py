from django.test import TestCase


class HomePageTest(TestCase):
    def test_smoke_test(self):
        self.assertEqual(1+1, 3)
