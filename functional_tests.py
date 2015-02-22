from selenium import webdriver

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
    self.fail('Finish the test!')

    # He is invited to enter a riddle of his own straight away

    # He types "When as door not a door?" into a question text box
    # He types "Think outside the box" into a hint text box
    # He types "When it's ajar!" into an answer text box

    # When He hits enter, the page updates, and now the page lists
    #  the riddle he just entered with all three lines of text

    # There is still a text box inviting him to add another riddle. He
    #  enters "What has four wheels and flys?" in the question, "Wrong
    #  spelling of flys" in the hint, and "A garbage truck!" in the answer

    # The page updates again, and now shows both riddles on the page

    # Eyrck wonders whether the site will remember his riddles. Then He sees
    # that the site has generated a unique URL for him -- there is some
    # explanatory text to that effect.

    # He visits that URL - his riddles are still there.

    # Satisfied, He goes back to sleep


if __name__ == '__main__':
  unittest.main(warnings='ignore')
