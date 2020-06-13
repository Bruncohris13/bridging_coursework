from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):  

    def setUp(self):  
        self.browser = webdriver.Firefox()

    def tearDown(self):  
        self.browser.quit()

    def test_start_page(self):  
        self.browser.get('http://localhost:8000')

        self.assertIn('Christos Efstathiou', self.browser.title)

    def test_button_to_edit_bio(self):
        self.browser.get('http://localhost:8000')

        self.browser.find_element_by_id("upload").click()
        self.assertIn("http://localhost:8000/bio_edit/", self.browser.current_url)

if __name__ == '__main__':  
    unittest.main(warnings='ignore')  
