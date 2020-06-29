from django.db import models
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify
from django.conf import settings
import os

class CvPdf(models.Model):
    cv_pdf = models.FileField(upload_to='cv/pdf/cv')


class Bio(models.Model):
    text = models.TextField()
    image = models.ImageField(upload_to='cv/img/profile')


class CVPost(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField(default="<p class='cv-post-text'> </p>")

    def formatted_markdown(self):
        return markdownify(self.text)

class EducationPost(CVPost):
    sub_title = models.CharField(max_length=100)

class WorkPost(CVPost):
    sub_title = models.CharField(max_length=100)

class AchievementPost(CVPost):
    pass

class QualificationPost(CVPost):
    pass


SKILL_CATEGORIES = (
    ('LANGUAGES', 'Languages'),
    ('PROGRAMMING_LANGUAGES', 'Programming Languages'),
    ('OTHER_PROGRAMMING_SKILLS', 'Other Programming Skills')
)

class SkillPost(models.Model):
    skill = models.CharField(max_length=50)
    category = models.CharField(max_length=150, choices=SKILL_CATEGORIES, default='PROGRAMMING_LANGUAGES')

class InterestPost(models.Model):
    interest = models.CharField(max_length=50)


class ProjectPost(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    image = models.ImageField(upload_to='cv/img/projects')
    url = models.URLField(max_length=300)

    def removeImage(self):
        os.remove(os.path.join(settings.MEDIA_ROOT, self.image.name))


class AddActivitiesPost(models.Model):
    text = models.TextField(default="<ul class='fa-ul cv-post-text'><li><i class='fa-li fa fa-users'></i> </li></ul>")

    def formatted_markdown(self):
        return markdownify(self.text)