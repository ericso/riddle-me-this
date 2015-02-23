from django.test import TestCase

from django.core.urlresolvers import resolve

from riddles.views import home_page


class HomePageTest(TestCase):

  def test_root_url_resolves_to_the_home_page(self):
    found = resolve('/')
    self.assertEqual(found.func, home_page)
