from django.db import models
from markdownx.utils import markdownify
from django.conf import settings
from ordered_model.models import OrderedModel
import os

class CvPdf(models.Model):
    cv_pdf = models.FileField(upload_to='cv/pdf/cv')

    def save(self, *args, **kwargs):
        try:
            this = CvPdf.objects.get(id=self.id)
            if this.cv_pdf != self.cv_pdf:
                this.cv_pdf.delete()
        except: pass
        super(CvPdf, self).save(*args, **kwargs)

class Bio(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()

    def formatted_markdown(self):
        return markdownify(self.text)


class CVPost(OrderedModel):
    title = models.CharField(max_length=100)
    text = models.TextField(default="<p class='cv-post-text'> </p>")

    def __str__(self):
        return self.title

    def formatted_markdown(self):
        return markdownify(self.text)

class EducationPost(CVPost):
    sub_title = models.CharField(max_length=100)

class ProfessionalEngagementsPost(CVPost):
    pass

class WorkProjectPost(CVPost):
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

class SkillPost(OrderedModel):
    skill = models.CharField(max_length=50)
    category = models.CharField(max_length=150, choices=SKILL_CATEGORIES, default='PROGRAMMING_LANGUAGES')

    def __str__(self):
        return self.skill

class InterestPost(OrderedModel):
    interest = models.CharField(max_length=50)

    def __str__(self):
        return self.interest


class ProjectPost(OrderedModel):
    title = models.CharField(max_length=100)
    text = models.TextField()
    image = models.ImageField(upload_to='cv/img/projects')
    url = models.URLField(max_length=300)

    def __str__(self):
        return self.title

    def removeImage(self):
        os.remove(os.path.join(settings.MEDIA_ROOT, self.image.name))
    
    def save(self, *args, **kwargs):
        try:
            this = ProjectPost.objects.get(id=self.id)
            if this.image != self.image:
                this.image.delete()
        except: pass
        super(ProjectPost, self).save(*args, **kwargs)


class AddActivitiesPost(OrderedModel):
    text = models.TextField(default="<ul class='fa-ul cv-post-text'><li><i class='fa-li fa fa-users'></i> </li></ul>")

    def __str__(self):
        return self.text

    def formatted_markdown(self):
        return markdownify(self.text)