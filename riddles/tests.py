from django.test import TestCase
from django.core.urlresolvers import resolve
from django.http import HttpRequest

from riddles.views import home_page


class HomePageTest(TestCase):

  def test_root_url_resolves_to_the_home_page(self):
    found = resolve('/')
    self.assertEqual(found.func, home_page)

  def test_home_page_returns_correct_html(self):
    request = HttpRequest()
    response = home_page(request)

    self.assertTrue(response.content.startswith(b'<html>'))
    self.assertIn(b'<title>Riddles</title>', response.content)
    self.assertTrue(response.content.endswith(b'</html>'))
