from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import secret
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
        # Go to the Admin Login Page
        self.browser.get('http://localhost:8000/admin')

        username_inputbox = self.browser.find_element_by_id('id_username')
        password_inputbox = self.browser.find_element_by_id('id_password')

        # Fill in the login boxes
        username_inputbox.send_keys(secret.username)
        password_inputbox.send_keys(secret.password)

        password_inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # Go back to the Home Page
        view_site = self.browser.find_element_by_xpath("//div[@id='user-tools']/a[1]")
        view_site.click()

    def test_home_page_navbar(self):
        # Go to the Home Page  
        self.browser.get('http://localhost:8000/')

        # Check if the title is correct
        self.assertIn('Christos Efstathiou', self.browser.title)

        navbar_brand = self.browser.find_element_by_class_name("navbar-brand")

        # Check if the Brand Title in the navbar is correct
        navbar_brand_text = navbar_brand.text
        self.assertIn('Christos Efstathiou', navbar_brand_text)

        # Check if the Brand Title link in the navbar is working
        navbar_brand.click()
        self.assertEqual('http://localhost:8000/', self.browser.current_url)

        navbar_links = self.browser.find_elements_by_class_name("nav-link")
        navbar_links_text = get_text_attribute(navbar_links)

        # Check if the navbbar links have the right names
        self.assertIn('Home', navbar_links_text)
        self.assertIn('Blog', navbar_links_text)

        # Check if the Home link works
        navbar_links[navbar_links_text.index('Home')].click()
        self.assertEqual('http://localhost:8000/', self.browser.current_url)

        navbar_links = self.browser.find_elements_by_class_name("nav-link")

        # Check if the Blog link works
        navbar_links[navbar_links_text.index('Blog')].click()
        self.assertEqual('http://localhost:8000/blog/', self.browser.current_url)
    
    def test_scrollspy(self):
        # Go to the Home Page 
        self.browser.get('http://localhost:8000')

        scrollspy = self.browser.find_elements_by_class_name('nav-link')
        scrollspy_text = get_text_attribute(scrollspy)

        # Check if the Scrollspy text is correct
        self.assertIn('Education', scrollspy_text)
        self.assertIn('Work Experience', scrollspy_text)
        self.assertIn('Achievements', scrollspy_text)
        self.assertIn('Qualifications', scrollspy_text)
        self.assertIn('Skills', scrollspy_text)
        self.assertIn('Interests', scrollspy_text)
        self.assertIn('Projects', scrollspy_text)
        self.assertIn('Additional Activities', scrollspy_text)
        self.assertIn('Contact Information', scrollspy_text)

        # Check if the Scrollspy links work
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
        # Login as Admin
        self.enableAdmin()

        # Add New Education Post
        education_title = self.browser.find_element_by_id('education')
        education_new = education_title.find_element_by_class_name("glyphicon-plus")
        education_new.click()

        # Check if the url is correct
        self.assertEqual("http://localhost:8000/cv_post_new/Education/", self.browser.current_url)

        title = self.browser.find_element_by_id("id_title")
        sub_title = self.browser.find_element_by_id("id_sub_title")
        text = self.browser.find_element_by_id("id_text")
        submit = self.browser.find_element_by_class_name("submit-text")

        # Complete the Form
        title.send_keys("Test Education Post")
        sub_title.send_keys("Subtitle")
        text.send_keys("Text for Education Post")
        submit.click()

        time.sleep(1)
    
        # Check if the new Post appears on the Home Page
        education_posts = self.browser.find_elements_by_id("education-post")

        self.assertIn('Test Education Post', education_posts[-1].find_element_by_class_name("cv-post-title").text)
        self.assertIn('Subtitle', education_posts[-1].find_element_by_class_name("cv-post-sub-title").text)
        self.assertIn('Text for Education Post', education_posts[-1].text)


        # Edit the new Post
        education_post_edit = education_posts[-1].find_element_by_class_name("glyphicon-pencil")
        education_post_edit.click()

        # Check if the url is correct
        self.assertIn("http://localhost:8000/cv_post_edit/Education/", self.browser.current_url)

        title = self.browser.find_element_by_id("id_title")
        sub_title = self.browser.find_element_by_id("id_sub_title")
        text = self.browser.find_element_by_id("id_text")
        submit = self.browser.find_element_by_class_name("submit-text")

        # Edit the Form
        title.send_keys(" [Edited]")
        sub_title.send_keys(" [Edited]")
        text.send_keys(" [Edited]")
        submit.click()

        time.sleep(1)

        # Check if the Edited Post has been edited on the Home Page
        education_posts = self.browser.find_elements_by_id("education-post")

        self.assertIn('Test Education Post [Edited]', education_posts[-1].find_element_by_class_name("cv-post-title").text)
        self.assertIn('Subtitle [Edited]', education_posts[-1].find_element_by_class_name("cv-post-sub-title").text)
        self.assertIn('Text for Education Post [Edited]', education_posts[-1].text)


        # Delete the new Post
        education_post_delete = education_posts[-1].find_element_by_class_name("close")
        education_post_delete.click()

        # Check if the New Post has been removed on the Home Page
        education_posts = self.browser.find_elements_by_id("education-post")

        self.assertNotIn('Test Education Post [Edited]', education_posts[-1].find_element_by_class_name("cv-post-title").text)
        self.assertNotIn('Subtitle [Edited]', education_posts[-1].find_element_by_class_name("cv-post-sub-title").text)
        self.assertNotIn('Text for Education Post [Edited]', education_posts[-1].text)

    def test_work(self):
        # Login as Admin
        self.enableAdmin()

        # Add New Work Experience Post
        work_title = self.browser.find_element_by_id('work')
        work_new = work_title.find_element_by_class_name("glyphicon-plus")
        work_new.click()

        # Check if the url is correct
        self.assertEqual("http://localhost:8000/cv_post_new/Work/", self.browser.current_url)

        title = self.browser.find_element_by_id("id_title")
        sub_title = self.browser.find_element_by_id("id_sub_title")
        text = self.browser.find_element_by_id("id_text")
        submit = self.browser.find_element_by_class_name("submit-text")

        # Complete the Form
        title.send_keys("Test Work Experience Post")
        sub_title.send_keys("Subtitle")
        text.send_keys("Text for Work Experience Post")
        submit.click()

        time.sleep(1)
    
        # Check if the new Post appears on the Home Page
        work_posts = self.browser.find_elements_by_id("work-post")

        self.assertIn('Test Work Experience Post', work_posts[-1].find_element_by_class_name("cv-post-title").text)
        self.assertIn('Subtitle', work_posts[-1].find_element_by_class_name("cv-post-sub-title").text)
        self.assertIn('Text for Work Experience Post', work_posts[-1].text)


        # Edit the new Post
        work_post_edit = work_posts[-1].find_element_by_class_name("glyphicon-pencil")
        work_post_edit.click()

        # Check if the url is correct
        self.assertIn("http://localhost:8000/cv_post_edit/Work/", self.browser.current_url)

        title = self.browser.find_element_by_id("id_title")
        sub_title = self.browser.find_element_by_id("id_sub_title")
        text = self.browser.find_element_by_id("id_text")
        submit = self.browser.find_element_by_class_name("submit-text")

        # Edit the Form
        title.send_keys(" [Edited]")
        sub_title.send_keys(" [Edited]")
        text.send_keys(" [Edited]")
        submit.click()

        time.sleep(1)

        # Check if the Edited Post has been edited on the Home Page
        work_posts = self.browser.find_elements_by_id("work-post")

        self.assertIn('Test Work Experience Post [Edited]', work_posts[-1].find_element_by_class_name("cv-post-title").text)
        self.assertIn('Subtitle [Edited]', work_posts[-1].find_element_by_class_name("cv-post-sub-title").text)
        self.assertIn('Text for Work Experience Post [Edited]', work_posts[-1].text)


        # Delete the new Post
        work_post_delete = work_posts[-1].find_element_by_class_name("close")
        work_post_delete.click()

        # Check if the New Post has been removed on the Home Page
        work_posts = self.browser.find_elements_by_id("education-post")

        self.assertNotIn('Test Work Experience Post [Edited]', work_posts[-1].find_element_by_class_name("cv-post-title").text)
        self.assertNotIn('Subtitle [Edited]', work_posts[-1].find_element_by_class_name("cv-post-sub-title").text)
        self.assertNotIn('Text for Work Experience Post [Edited]', work_posts[-1].text)

    def test_achievements(self):
        # Login as Admin
        self.enableAdmin()

        # Add New Achievements Post
        achievements_title = self.browser.find_element_by_id('achievements')
        achievements_new = achievements_title.find_element_by_class_name("glyphicon-plus")
        achievements_new.click()

        # Check if the url is correct
        self.assertEqual("http://localhost:8000/cv_post_new/Achievement/", self.browser.current_url)

        title = self.browser.find_element_by_id("id_title")
        text = self.browser.find_element_by_id("id_text")
        submit = self.browser.find_element_by_class_name("submit-text")

        # Complete the Form
        title.send_keys("Test Achievement Post")
        text.send_keys("Text for Achievement Post")
        submit.click()

        time.sleep(1)
    
        # Check if the new Post appears on the Home Page
        achievement_posts = self.browser.find_elements_by_id("achievement-post")

        self.assertIn('Test Achievement Post', achievement_posts[-1].find_element_by_class_name("cv-post-title").text)
        self.assertIn('Text for Achievement Post', achievement_posts[-1].text)


        # Edit the new Post
        achievement_post_edit = achievement_posts[-1].find_element_by_class_name("glyphicon-pencil")
        achievement_post_edit.click()

        # Check if the url is correct
        self.assertIn("http://localhost:8000/cv_post_edit/Achievement/", self.browser.current_url)

        title = self.browser.find_element_by_id("id_title")
        text = self.browser.find_element_by_id("id_text")
        submit = self.browser.find_element_by_class_name("submit-text")

        # Edit the Form
        title.send_keys(" [Edited]")
        text.send_keys(" [Edited]")
        submit.click()

        time.sleep(1)

        # Check if the Edited Post has been edited on the Home Page
        achievement_posts = self.browser.find_elements_by_id("achievement-post")

        self.assertIn('Test Achievement Post [Edited]', achievement_posts[-1].find_element_by_class_name("cv-post-title").text)
        self.assertIn('Text for Achievement Post [Edited]', achievement_posts[-1].text)


        # Delete the new Post
        achievement_post_delete = achievement_posts[-1].find_element_by_class_name("close")
        achievement_post_delete.click()

        # Check if the New Post has been removed on the Home Page
        achievement_posts = self.browser.find_elements_by_id("achievement-post")

        self.assertNotIn('Test Achievement Post [Edited]', achievement_posts[-1].find_element_by_class_name("cv-post-title").text)
        self.assertNotIn('Text for Achievement Post [Edited]', achievement_posts[-1].text)


if __name__ == '__main__':  
    unittest.main(warnings='ignore')  