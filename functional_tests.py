from selenium import webdriver
import unittest


class HomePageTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_home_page(self):
        # Edit hears about a cool todo list site, she visits it
        self.browser.get('http://localhost:8000')

        # She sees the title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        header = self.browser.find_element_by_tag_name('h1')
        self.assertIn('To-Do', header.text)

        # She is invited to enter a to-do item straight away
        self.fail('finish the test')

        # She types "buy peacock feathers" into a text box(Edith's hobby is
        # tying fly-fishing lures)

        # when she hits enter, the page updates, and now the page lists
        # "1: buy peacock feathers" as an item in a to-do list

        # There is still a text box inviting ehr to add another item. She
        # enters "Use peacock feather to make a fly" (Edit is very methodical)

        # the page updates again, and now shows both items on her list

        # Edit wonders whether the site will remember her list. Then she sees
        # that the site has generated a unique URL for her -- there is some
        # explanatory text to that effect


if __name__ == '__main__':
    unittest.main()
