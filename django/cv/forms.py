from django import forms
from .models import *

class CvPdfForm(forms.ModelForm):
    class Meta:
        model = CvPdf
        fields = ('cv_pdf',)


class QuoteForm(forms.ModelForm):
    class Meta:
        model = Quote
        fields = ('text',)


class CVPostForm(forms.ModelForm):
    class Meta:
        model = CVPost
        fields = ('title', 'text')

class EducationPostForm(CVPostForm):
    class Meta(CVPostForm.Meta):
        model = EducationPost
        fields = CVPostForm.Meta.fields + ('sub_title',)
    field_order = ('title', 'sub_title', 'text')

class WorkPostForm(CVPostForm):
    class Meta(CVPostForm.Meta):
        model = WorkPost
        fields = CVPostForm.Meta.fields + ('sub_title',)
    field_order = ('title', 'sub_title', 'text')

class AchievementPostForm(CVPostForm):
    class Meta(CVPostForm.Meta):
        model = AchievementPost

class QualificationPostForm(CVPostForm):
    class Meta(CVPostForm.Meta):
        model = QualificationPost


class SkillPostForm(forms.ModelForm):
    class Meta:
        model = SkillPost
        fields = ('skill', 'category')

class InterestPostForm(forms.ModelForm):
    class Meta:
        model = InterestPost
        fields = ('interest',)


class ProjectPostForm(forms.ModelForm):
    class Meta:
        model = ProjectPost
        fields = ('title', 'text', 'image', 'url')


class AddActivitiesPostForm(forms.ModelForm):
    class Meta:
        model = AddActivitiesPost
        fields = ('text',)