from django import forms
from .models import *

class BioForm(forms.ModelForm):
    class Meta:
            model = Bio
            fields = ('text', 'image')

class CVPostForm(forms.ModelForm):
    class Meta:
            model = EducationPost
            fields = ('title', 'sub_title', 'text')