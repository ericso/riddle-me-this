from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest


class NewVisitorTest(unittest.TestCase):

  def setUp(self):
    self.browser = webdriver.Chrome()
    self.browser.implicitly_wait(3)

  def tearDown(self):
    self.browser.quit()

  def test_can_enter_riddles_and_retrieve_them_later(self):

    # Eyrck has heard about a cool new online riddles app. He goes
    # to check out its homepage
    self.browser.get('http://localhost:8000')

    # He notices the page title and header mention riddles
    self.assertIn('Riddles', self.browser.title)
    header_text = self.browser.find_element_by_tag_name('h1').text
    self.assertIn('Riddles', header_text)

    # He is invited to enter a riddle of his own straight away
    inputbox = self.browser.find_element_by_id('id_new_riddle')
    self.assertEqual(
      inputbox.get_attribute('placeholder'),
      'Enter a riddle'
    )

    # He types "When is door not a door?" into a question text box
    # He types "Think outside the box" into a hint text box
    # He types "When it's ajar!" into an answer text box
    inputbox.send_keys('When is door not a door?')

    # When He hits enter, the page updates, and now the page lists
    #  the riddle he just entered with all three lines of text
    inputbox.send_keys(Keys.ENTER)

    table = self.browser.find_element_by_id('id_riddles_table')
    rows = table.find_elements_by_tag_name('tr')
    self.assertTrue(
      any(row.text == 'When is a door not a door?' for row in rows),
      "New riddle did not appear in table"
    )

    # There is still a text box inviting him to add another riddle. He
    #  enters "What has four wheels and flys?" in the question, "Wrong
    #  spelling of flys" in the hint, and "A garbage truck!" in the answer
    self.fail('Finish the test!')

    # The page updates again, and now shows both riddles on the page

    # Eyrck wonders whether the site will remember his riddles. Then He sees
    # that the site has generated a unique URL for him -- there is some
    # explanatory text to that effect.

    # He visits that URL - his riddles are still there.

    # Satisfied, He goes back to sleep


if __name__ == '__main__':
  unittest.main(warnings='ignore')
