from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import secret
import unittest
import time
import os

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

        # Check if the url is correct
        self.assertEqual("http://localhost:8000/", self.browser.current_url)
    
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

        # Check if the url is correct
        self.assertEqual("http://localhost:8000/", self.browser.current_url)

        # Check if the Edited Post has been edited on the Home Page
        education_posts = self.browser.find_elements_by_id("education-post")

        self.assertIn('Test Education Post [Edited]', education_posts[-1].find_element_by_class_name("cv-post-title").text)
        self.assertIn('Subtitle [Edited]', education_posts[-1].find_element_by_class_name("cv-post-sub-title").text)
        self.assertIn('Text for Education Post [Edited]', education_posts[-1].text)


        # Delete the new Post
        education_post_delete = education_posts[-1].find_element_by_class_name("close")
        education_post_delete.click()

        # Check if the url is correct
        self.assertEqual("http://localhost:8000/", self.browser.current_url)

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

        # Check if the url is correct
        self.assertEqual("http://localhost:8000/", self.browser.current_url)
    
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

        # Check if the url is correct
        self.assertEqual("http://localhost:8000/", self.browser.current_url)

        # Check if the Edited Post has been edited on the Home Page
        work_posts = self.browser.find_elements_by_id("work-post")

        self.assertIn('Test Work Experience Post [Edited]', work_posts[-1].find_element_by_class_name("cv-post-title").text)
        self.assertIn('Subtitle [Edited]', work_posts[-1].find_element_by_class_name("cv-post-sub-title").text)
        self.assertIn('Text for Work Experience Post [Edited]', work_posts[-1].text)


        # Delete the new Post
        work_post_delete = work_posts[-1].find_element_by_class_name("close")
        work_post_delete.click()

        # Check if the url is correct
        self.assertEqual("http://localhost:8000/", self.browser.current_url)

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

        # Check if the url is correct
        self.assertEqual("http://localhost:8000/", self.browser.current_url)
    
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

        # Check if the url is correct
        self.assertEqual("http://localhost:8000/", self.browser.current_url)

        # Check if the Edited Post has been edited on the Home Page
        achievement_posts = self.browser.find_elements_by_id("achievement-post")

        self.assertIn('Test Achievement Post [Edited]', achievement_posts[-1].find_element_by_class_name("cv-post-title").text)
        self.assertIn('Text for Achievement Post [Edited]', achievement_posts[-1].text)


        # Delete the new Post
        achievement_post_delete = achievement_posts[-1].find_element_by_class_name("close")
        achievement_post_delete.click()

        # Check if the url is correct
        self.assertEqual("http://localhost:8000/", self.browser.current_url)

        # Check if the New Post has been removed on the Home Page
        achievement_posts = self.browser.find_elements_by_id("achievement-post")

        self.assertNotIn('Test Achievement Post [Edited]', achievement_posts[-1].find_element_by_class_name("cv-post-title").text)
        self.assertNotIn('Text for Achievement Post [Edited]', achievement_posts[-1].text)

    def test_qualifications(self):
        # Login as Admin
        self.enableAdmin()

        # Add New Qualifications Post
        qualifications_title = self.browser.find_element_by_id('qualifications')
        qualifications_new = qualifications_title.find_element_by_class_name("glyphicon-plus")
        qualifications_new.click()

        # Check if the url is correct
        self.assertEqual("http://localhost:8000/cv_post_new/Qualification/", self.browser.current_url)

        title = self.browser.find_element_by_id("id_title")
        text = self.browser.find_element_by_id("id_text")
        submit = self.browser.find_element_by_class_name("submit-text")

        # Complete the Form
        title.send_keys("Test Qualification Post")
        text.send_keys("Text for Qualification Post")
        submit.click()

        time.sleep(1)

        # Check if the url is correct
        self.assertEqual("http://localhost:8000/", self.browser.current_url)
    
        # Check if the new Post appears on the Home Page
        qualification_posts = self.browser.find_elements_by_id("qualification-post")

        self.assertIn('Test Qualification Post', qualification_posts[-1].find_element_by_class_name("cv-post-title").text)
        self.assertIn('Text for Qualification Post', qualification_posts[-1].text)


        # Edit the new Post
        qualification_post_edit = qualification_posts[-1].find_element_by_class_name("glyphicon-pencil")
        qualification_post_edit.click()

        # Check if the url is correct
        self.assertIn("http://localhost:8000/cv_post_edit/Qualification/", self.browser.current_url)

        title = self.browser.find_element_by_id("id_title")
        text = self.browser.find_element_by_id("id_text")
        submit = self.browser.find_element_by_class_name("submit-text")

        # Edit the Form
        title.send_keys(" [Edited]")
        text.send_keys(" [Edited]")
        submit.click()

        time.sleep(1)

        # Check if the url is correct
        self.assertEqual("http://localhost:8000/", self.browser.current_url)

        # Check if the Edited Post has been edited on the Home Page
        qualification_posts = self.browser.find_elements_by_id("qualification-post")

        self.assertIn('Test Qualification Post [Edited]', qualification_posts[-1].find_element_by_class_name("cv-post-title").text)
        self.assertIn('Text for Qualification Post [Edited]', qualification_posts[-1].text)


        # Delete the new Post
        qualification_post_delete = qualification_posts[-1].find_element_by_class_name("close")
        qualification_post_delete.click()

        # Check if the url is correct
        self.assertEqual("http://localhost:8000/", self.browser.current_url)

        # Check if the New Post has been removed on the Home Page
        qualification_posts = self.browser.find_elements_by_id("qualification-post")

        self.assertNotIn('Test Qualification Post [Edited]', qualification_posts[-1].find_element_by_class_name("cv-post-title").text)
        self.assertNotIn('Text for Qualification Post [Edited]', qualification_posts[-1].text)

    def test_skills(self):
        # Login as Admin
        self.enableAdmin()

        skill_categories = {
            "Languages": "languages",
            "Programming Languages": "programming_languages",
            "Other Programming Skills": "other_prog_skills",
        }

        # Add New Skill Post for everty category
        for i, k in enumerate(skill_categories):

            # Add New Skill Post
            skills_title = self.browser.find_element_by_id('skills')
            skills_new = skills_title.find_element_by_class_name("glyphicon-plus")
            skills_new.click()

            # Check if the url is correct
            self.assertEqual("http://localhost:8000/cv_post_new/Skill/", self.browser.current_url)

            skill = self.browser.find_element_by_id("id_skill")
            category = self.browser.find_element_by_id("id_category")
            submit = self.browser.find_element_by_class_name("submit-text")

            # Complete the Form each time with a Different Category         
            category.click()
            category_option = category.find_elements_by_tag_name("option")
            category_option[i].click()

            skill.send_keys("Test Skill Post " + category_option[i].text)

            submit.click()

            time.sleep(1)

            # Check if the url is correct
            self.assertEqual("http://localhost:8000/", self.browser.current_url)
    
        # Check if the new Posts appear on the Home Page
        for skill_name, skill_id in skill_categories.items():
            skills_posts = self.browser.find_elements_by_id(skill_id)

            self.assertIn('Test Skill Post ' + skill_name, skills_posts[-1].find_element_by_class_name("skill-text").text)


        # Edit the new Posts
        for skill_name, skill_id in skill_categories.items():
            skills_posts = self.browser.find_elements_by_id(skill_id)

            skill_post_edit = skills_posts[-1].find_element_by_class_name("glyphicon-pencil")
            skill_post_edit.click()

            # Check if the url is correct
            self.assertIn("http://localhost:8000/cv_post_edit/Skill/", self.browser.current_url)

            skill = self.browser.find_element_by_id("id_skill")
            category = self.browser.find_element_by_id("id_category")
            submit = self.browser.find_element_by_class_name("submit-text")

            # Edit the Form
            skill.send_keys(" [Edited]")
            submit.click()

            time.sleep(1)

            # Check if the url is correct
            self.assertEqual("http://localhost:8000/", self.browser.current_url)

        # Check if the Edited Posts have been edited on the Home Page
        for skill_name, skill_id in skill_categories.items():
            skills_posts = self.browser.find_elements_by_id(skill_id)

            self.assertIn('Test Skill Post ' + skill_name + ' [Edited]', skills_posts[-1].find_element_by_class_name("skill-text").text)


        # Delete the new Posts
        for skill_name, skill_id in skill_categories.items():
            skills_posts = self.browser.find_elements_by_id(skill_id)

            skill_post_delete = skills_posts[-1].find_element_by_class_name("close")
            skill_post_delete.click()

            # Check if the url is correct
            self.assertEqual("http://localhost:8000/", self.browser.current_url)

        # Check if the New Posts have been removed on the Home Page
        for skill_name, skill_id in skill_categories.items():
            skills_posts = self.browser.find_elements_by_id(skill_id)

            self.assertNotIn('Test Skill Post ' + skill_name + ' [Edited]', skills_posts[-1].find_element_by_class_name("skill-text").text)

    def test_skill_change_category(self):
        # Login as Admin
        self.enableAdmin()

        # Add New Skill Post
        skills_title = self.browser.find_element_by_id('skills')
        skills_new = skills_title.find_element_by_class_name("glyphicon-plus")
        skills_new.click()

        # Check if the url is correct
        self.assertEqual("http://localhost:8000/cv_post_new/Skill/", self.browser.current_url)

        skill = self.browser.find_element_by_id("id_skill")
        category = self.browser.find_element_by_id("id_category")
        submit = self.browser.find_element_by_class_name("submit-text")

        # Complete the Form with category 'Language'
        category.click()
        category_option = category.find_elements_by_tag_name("option")
        category_option[0].click()

        skill.send_keys("Test Skill Post")

        submit.click()

        time.sleep(1)

        # Check if the url is correct
        self.assertEqual("http://localhost:8000/", self.browser.current_url)

        # Check if the new Post appears on the Home Page
        skills_posts_language = self.browser.find_elements_by_id('languages')

        self.assertIn('Test Skill Post', skills_posts_language[-1].find_element_by_class_name("skill-text").text)


        # Edit the new Post  
        skill_post_edit = skills_posts_language[-1].find_element_by_class_name("glyphicon-pencil")
        skill_post_edit.click()

        # Check if the url is correct
        self.assertIn("http://localhost:8000/cv_post_edit/Skill/", self.browser.current_url)

        skill = self.browser.find_element_by_id("id_skill")
        category = self.browser.find_element_by_id("id_category")
        submit = self.browser.find_element_by_class_name("submit-text")

        # Edit the Form and change the Skill Category to 'Programming Languages'
        skill.send_keys(" [Edited]")

        category.click()
        category_option = category.find_elements_by_tag_name("option")
        category_option[1].click()

        submit.click()

        time.sleep(1)

        # Check if the url is correct
        self.assertEqual("http://localhost:8000/", self.browser.current_url)

        # Check if the Edited Post has been edited on the Home Page
        skills_posts_prog_lang = self.browser.find_elements_by_id('programming_languages')

        self.assertIn('Test Skill Post [Edited]', skills_posts_prog_lang[-1].find_element_by_class_name("skill-text").text)

        # Delete the new Post
        skill_post_delete = skills_posts_prog_lang[-1].find_element_by_class_name("close")
        skill_post_delete.click()

        # Check if the url is correct
        self.assertEqual("http://localhost:8000/", self.browser.current_url)

        # Check if the New Post has been removed on the Home Page from both categories
        skills_posts_prog_lang = self.browser.find_elements_by_id('programming_languages')
        skills_posts_languages = self.browser.find_elements_by_id('languages')

        self.assertNotIn('Test Skill Post [Edited]', skills_posts_prog_lang[-1].find_element_by_class_name("skill-text").text)
        self.assertNotIn('Test Skill Post [Edited]', skills_posts_languages[-1].find_element_by_class_name("skill-text").text)

    def test_interests(self):
        # Login as Admin
        self.enableAdmin()

        # Add New Interest Post
        interests_title = self.browser.find_element_by_id('interests')
        interests_new = interests_title.find_element_by_class_name("glyphicon-plus")
        interests_new.click()

        # Check if the url is correct
        self.assertEqual("http://localhost:8000/cv_post_new/Interest/", self.browser.current_url)

        interest = self.browser.find_element_by_id("id_interest")
        submit = self.browser.find_element_by_class_name("submit-text")

        # Complete the Form
        interest.send_keys("Test Interest Post")
        submit.click()

        time.sleep(1)

        # Check if the url is correct
        self.assertEqual("http://localhost:8000/", self.browser.current_url)

        # Check if the new Post appears on the Home Page
        interests_posts = self.browser.find_elements_by_class_name('interest-post')

        self.assertIn('Test Interest Post', interests_posts[-1].find_element_by_class_name("interest-text").text)


        # Edit the new Post  
        interest_post_edit = interests_posts[-1].find_element_by_class_name("glyphicon-pencil")
        interest_post_edit.click()

        # Check if the url is correct
        self.assertIn("http://localhost:8000/cv_post_edit/Interest/", self.browser.current_url)

        interest = self.browser.find_element_by_id("id_interest")
        submit = self.browser.find_element_by_class_name("submit-text")

        # Edit the Form
        interest.send_keys(" [Edited]")
        submit.click()

        time.sleep(1)

        # Check if the url is correct
        self.assertEqual("http://localhost:8000/", self.browser.current_url)

        # Check if the Edited Post has been edited on the Home Page
        interests_posts = self.browser.find_elements_by_class_name('interest-post')

        self.assertIn('Test Interest Post [Edited]', interests_posts[-1].find_element_by_class_name("interest-text").text)

        # Delete the new Post
        interest_post_delete = interests_posts[-1].find_element_by_class_name("close")
        interest_post_delete.click()

        # Check if the url is correct
        self.assertEqual("http://localhost:8000/", self.browser.current_url)

        # Check if the New Post has been removed on the Home Page
        interests_posts = self.browser.find_elements_by_class_name('interest-post')

        self.assertNotIn('Test Interest Post [Edited]', interests_posts[-1].find_element_by_class_name("interest-text").text)

    def test_projects(self):
        # Login as Admin
        self.enableAdmin()

        # Add New Project Post
        projects_title = self.browser.find_element_by_id('projects')
        project_new = projects_title.find_element_by_class_name("glyphicon-plus")
        project_new.click()

        # Check if the url is correct
        self.assertEqual("http://localhost:8000/cv_post_new/Project/", self.browser.current_url)

        title = self.browser.find_element_by_id("id_title")
        text = self.browser.find_element_by_id("id_text")
        image = self.browser.find_element_by_id("id_image")
        url = self.browser.find_element_by_id("id_url")
        submit = self.browser.find_element_by_class_name("submit-text")

        # Complete the Form
        title.send_keys("Test Project Post")
        text.send_keys("Text for Project Post")
        image.send_keys(os.getcwd()+"\\test_project.jpg")
        url.send_keys("https://www.google.com/")
        submit.click()

        time.sleep(1)

        # Check if the url is correct
        self.assertEqual("http://localhost:8000/", self.browser.current_url)
    
        # Check if the new Post appears on the Home Page
        project_posts = self.browser.find_elements_by_class_name("project-card")

        self.assertIn('Test Project Post', project_posts[-1].find_element_by_class_name("cv-post-title").text)
        self.assertIn('Text for Project Post', project_posts[-1].find_element_by_class_name("cv-post-text").text)
        self.assertIn("test_project.jpg", project_posts[-1].find_element_by_class_name("card-img-top").get_attribute('src'))

        # Check if the Project link works
        project_posts[-1].click()
        time.sleep(5)

        # Change Tab
        self.browser.switch_to.window(self.browser.window_handles[1])

        # Check if the url is correct
        self.assertIn("https://www.google.com/", self.browser.current_url)

        # Go back to First Tab
        self.browser.switch_to.window(self.browser.window_handles[0])


        # Edit the new Post
        project_post_edit = project_posts[-1].find_element_by_class_name("glyphicon-pencil")
        project_post_edit.click()

        # Check if the url is correct
        self.assertIn("http://localhost:8000/cv_post_edit/Project/", self.browser.current_url)

        title = self.browser.find_element_by_id("id_title")
        text = self.browser.find_element_by_id("id_text")
        image = self.browser.find_element_by_id("id_image")
        url = self.browser.find_element_by_id("id_url")
        submit = self.browser.find_element_by_class_name("submit-text")

        # Edit the Form
        title.send_keys(" [Edited]")
        text.send_keys(" [Edited]")
        image.send_keys(os.getcwd()+"\\test_project_Edited.jpg")
        url.clear()
        url.send_keys("https://www.youtube.com/")
        submit.click()

        time.sleep(1)

        # Check if the url is correct
        self.assertEqual("http://localhost:8000/", self.browser.current_url)

        # Check if the Edited Post has been edited on the Home Page
        project_posts = self.browser.find_elements_by_class_name("project-card")

        self.assertIn('Test Project Post [Edited]', project_posts[-1].find_element_by_class_name("cv-post-title").text)
        self.assertIn('Text for Project Post [Edited]', project_posts[-1].find_element_by_class_name("cv-post-text").text)
        self.assertIn("test_project_Edited.jpg", project_posts[-1].find_element_by_class_name("card-img-top").get_attribute('src'))

        # Check if the Project link works
        project_posts[-1].click()
        time.sleep(5)

        # Change Tab
        self.browser.switch_to.window(self.browser.window_handles[1])

        # Check if the url is correct
        self.assertIn("https://www.youtube.com/", self.browser.current_url)

        # Go back to First Tab
        self.browser.switch_to.window(self.browser.window_handles[0])


        # Delete the new Post
        education_post_delete = project_posts[-1].find_element_by_class_name("close")
        education_post_delete.click()

        # Check if the url is correct
        self.assertEqual("http://localhost:8000/", self.browser.current_url)

        # Check if the New Post has been removed on the Home Page
        project_posts = self.browser.find_elements_by_class_name("project-card")

        self.assertNotIn('Test Project Post [Edited]', project_posts[-1].find_element_by_class_name("cv-post-title").text)
        self.assertNotIn('Text for Project Post [Edited]', project_posts[-1].find_element_by_class_name("cv-post-text").text)
        self.assertNotIn("test_project_Edited.jpg", project_posts[-1].find_element_by_class_name("card-img-top").get_attribute('src'))

    def test_add_activities(self):
        # Login as Admin
        self.enableAdmin()

        # Add New Additional Activities Post
        add_activities_title = self.browser.find_element_by_id('add_activities')
        add_activities_new = add_activities_title.find_element_by_class_name("glyphicon-plus")
        add_activities_new.click()

        # Check if the url is correct
        self.assertEqual("http://localhost:8000/cv_post_new/Add_Activities/", self.browser.current_url)

        text = self.browser.find_element_by_id("id_text")
        submit = self.browser.find_element_by_class_name("submit-text")

        # Complete the Form
        text.send_keys("Text for Additional Activities Post")
        submit.click()

        time.sleep(1)

        # Check if the url is correct
        self.assertEqual("http://localhost:8000/", self.browser.current_url)
    
        # Check if the new Post appears on the Home Page
        add_activities_posts = self.browser.find_elements_by_id("add-activities-post")

        self.assertIn('Text for Additional Activities Post', add_activities_posts[-1].text)


        # Edit the new Post
        add_activities_post_edit = add_activities_posts[-1].find_element_by_class_name("glyphicon-pencil")
        add_activities_post_edit.click()

        # Check if the url is correct
        self.assertIn("http://localhost:8000/cv_post_edit/Add_Activities/", self.browser.current_url)

        text = self.browser.find_element_by_id("id_text")
        submit = self.browser.find_element_by_class_name("submit-text")

        # Edit the Form
        text.send_keys(" [Edited]")
        submit.click()

        time.sleep(1)

        # Check if the url is correct
        self.assertEqual("http://localhost:8000/", self.browser.current_url)

        # Check if the Edited Post has been edited on the Home Page
        add_activities_posts = self.browser.find_elements_by_id("add-activities-post")

        self.assertIn('Text for Additional Activities Post [Edited]', add_activities_posts[-1].text)


        # Delete the new Post
        add_activities_post_delete = add_activities_posts[-1].find_element_by_class_name("close")
        add_activities_post_delete.click()

        # Check if the url is correct
        self.assertEqual("http://localhost:8000/", self.browser.current_url)

        # Check if the New Post has been removed on the Home Page
        add_activities_posts = self.browser.find_elements_by_id("add-activities-post")

        self.assertNotIn('Text for Additional Activities Post [Edited]', add_activities_posts[-1].text)

    def test_contact(self):
        # Go to the Home Page  
        self.browser.get('http://localhost:8000/')

        # Check if the Email link is correct
        email_link = self.browser.find_element_by_class_name("fa-envelope")
        self.assertIn('cefstathiou13@gmail.com', email_link.get_attribute('href'))


        # Check if the Linkedin link is correct (Cannot check if it is working, because it needs verification)
        linkedin_link = self.browser.find_element_by_class_name("fa-linkedin")
        self.assertIn('https://www.linkedin.com/in/christos-efstathiou/', linkedin_link.get_attribute('onclick'))


        # Check if the Github link is correct
        github_link = self.browser.find_element_by_class_name("fa-github")
        self.assertIn('https://github.com/Brunochris13', github_link.get_attribute('onclick'))

        # Check if the Github link is working
        github_link.click()
        time.sleep(5)

        # Change Tab
        self.browser.switch_to.window(self.browser.window_handles[1])

        # Check if the URL of the New Tab is correct
        self.assertEqual('https://github.com/Brunochris13', self.browser.current_url)


        # Check if the CV PDF link is correct

        # Change Back to First Tab
        self.browser.switch_to.window(self.browser.window_handles[0])

        pdf_link = self.browser.find_element_by_class_name("fa-file-text")
        print('PDF: ' + pdf_link.get_attribute('href'))
        self.assertIn('Christos_Efstathiou_CV', pdf_link.get_attribute('href'))


if __name__ == '__main__':  
    unittest.main(warnings='ignore')  