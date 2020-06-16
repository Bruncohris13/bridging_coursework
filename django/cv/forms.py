from django import forms
from .models import *

class BioForm(forms.ModelForm):
    class Meta:
        model = Bio
        fields = ('text', 'image')

class CVPostForm(forms.ModelForm):
    class Meta:
        model = CVPost
        fields = ('title', 'text')

class EducationPostForm(CVPostForm):
    class Meta(CVPostForm.Meta):
        model = EducationPost
        fields = CVPostForm.Meta.fields + ('sub_title',)
    field_order = ('title', 'sub_title', 'text')