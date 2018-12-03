import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class HomePageTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edit hears about a cool todo list site, she visits it
        self.browser.get('http://localhost:8000')

        # She sees the title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        header = self.browser.find_element_by_tag_name('h1')
        self.assertIn('To-Do', header.text)

        # She is invited to enter a to-do item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # She types "buy peacock feathers" into a text box(Edith's hobby is
        # tying fly-fishing lures)
        inputbox.send_keys('Buy peacock featers')

        # when she hits enter, the page updates, and now the page lists
        # "1: buy peacock feathers" as an item in a to-do list
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element_by_tag_name('table')
        # table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_element_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Buy peacock feathers' for row in rows),
            "New to-do item did not appear in table"
        )

        # There is still a text box inviting ehr to add another item. She
        # enters "Use peacock feather to make a fly" (Edit is very methodical)
        self.fail('all-passed: finish the test')

        # the page updates again, and now shows both items on her list

        # Edit wonders whether the site will remember her list. Then she sees
        # that the site has generated a unique URL for her -- there is some
        # explanatory text to that effect


if __name__ == '__main__':
    unittest.main()
