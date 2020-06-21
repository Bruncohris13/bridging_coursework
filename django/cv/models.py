from django.db import models

class CvPdf(models.Model):
    cv_pdf = models.FileField(upload_to='cv/pdf/cv')


class Bio(models.Model):
    text = models.TextField()
    image = models.ImageField(upload_to='cv/img/profile')


class CVPost(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()

class EducationPost(CVPost):
    sub_title = models.CharField(max_length=100)

class WorkPost(CVPost):
    sub_title = models.CharField(max_length=100)

class AchievementPost(CVPost):
    pass

class QualificationPost(CVPost):
    pass


class SkillPost(models.Model):
    skill = models.CharField(max_length=50)

class InterestPost(models.Model):
    interest = models.CharField(max_length=50)


class ProjectPost(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    image = models.ImageField(upload_to='cv/img/projects')
    url = models.URLField(max_length=300)