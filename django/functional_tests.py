from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time

def get_text_attribute(links):
        result = []
        for item in links:
            result.append(item.text)
        return result

class MyTests(unittest.TestCase):  

    def setUp(self):  
        self.browser = webdriver.Firefox()

    def tearDown(self):  
        self.browser.quit()

    def enableAdmin(self):
        self.browser.get('http://localhost:8000/admin')
        username_inputbox = self.browser.find_element_by_id('id_username')
        password_inputbox = self.browser.find_element_by_id('id_password')

        username_inputbox.send_keys('brunochris13')
        password_inputbox.send_keys('Chris-bruno13')

        password_inputbox.send_keys(Keys.ENTER)

        view_site = self.browser.find_element_by_xpath("//div[@id='user-tools']/a[1]")
        view_site.click()

    def test_home_page_navbar(self):  
        self.browser.get('http://localhost:8000/admin/')

        self.assertIn('Christos Efstathiou', self.browser.title)

        navbar_brand = self.browser.find_element_by_class_name("navbar-brand")

        navbar_brand_text = navbar_brand.text
        self.assertIn('Christos Efstathiou', navbar_brand_text)

        navbar_brand.click()
        self.assertEqual('http://localhost:8000/', self.browser.current_url)

        navbar_links = self.browser.find_elements_by_class_name("nav-link")
        navbar_links_text = get_text_attribute(navbar_links)

        self.assertIn('Home', navbar_links_text)
        self.assertIn('Blog', navbar_links_text)

        navbar_links[navbar_links_text.index('Home')].click()
        self.assertEqual('http://localhost:8000/', self.browser.current_url)

        navbar_links = self.browser.find_elements_by_class_name("nav-link")

        navbar_links[navbar_links_text.index('Blog')].click()
        self.assertEqual('http://localhost:8000/blog/', self.browser.current_url)
    
    def test_scrollspy(self):
        self.browser.get('http://localhost:8000')

        scrollspy = self.browser.find_elements_by_class_name('nav-link')
        scrollspy_text = get_text_attribute(scrollspy)

        self.assertIn('Education', scrollspy_text)
        self.assertIn('Work Experience', scrollspy_text)
        self.assertIn('Achievements', scrollspy_text)
        self.assertIn('Qualifications', scrollspy_text)
        self.assertIn('Skills', scrollspy_text)
        self.assertIn('Interests', scrollspy_text)
        self.assertIn('Projects', scrollspy_text)
        self.assertIn('Additional Activities', scrollspy_text)
        self.assertIn('Contact Information', scrollspy_text)

        scrollspy[scrollspy_text.index('Education')].click()
        self.assertEqual('http://localhost:8000/#education', self.browser.current_url)
        scrollspy[scrollspy_text.index('Work Experience')].click()
        self.assertEqual('http://localhost:8000/#work', self.browser.current_url)
        scrollspy[scrollspy_text.index('Achievements')].click()
        self.assertEqual('http://localhost:8000/#achievements', self.browser.current_url)
        scrollspy[scrollspy_text.index('Qualifications')].click()
        self.assertEqual('http://localhost:8000/#qualifications', self.browser.current_url)
        scrollspy[scrollspy_text.index('Skills')].click()
        self.assertEqual('http://localhost:8000/#skills', self.browser.current_url)
        scrollspy[scrollspy_text.index('Interests')].click()
        self.assertEqual('http://localhost:8000/#interests', self.browser.current_url)
        scrollspy[scrollspy_text.index('Projects')].click()
        self.assertEqual('http://localhost:8000/#projects', self.browser.current_url)
        scrollspy[scrollspy_text.index('Additional Activities')].click()
        self.assertEqual('http://localhost:8000/#add_activities', self.browser.current_url)
        scrollspy[scrollspy_text.index('Contact Information')].click()
        self.assertEqual('http://localhost:8000/#contact', self.browser.current_url)
    
    def test_education(self):
        self.enableAdmin()
        # self.browser.get('http://localhost:8000')

        education_new = self.browser.find_element_by_id('education_new')

if __name__ == '__main__':  
    unittest.main(warnings='ignore')  