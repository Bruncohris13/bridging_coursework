from django.test import TestCase
from .views import home_page
from django.urls import resolve

# Create your tests here.
class HomePageTests(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')  
        self.assertEqual(found.func, home_page)

    def test_upload_button(self):
        found = resolve('/')