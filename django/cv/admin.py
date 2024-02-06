from django.contrib import admin
from ordered_model.admin import OrderedModelAdmin
from .models import *

class CVPostOrderedAdmin(OrderedModelAdmin):
    list_display = ('title', 'move_up_down_links')

class SkillPostOrderedAdmin(OrderedModelAdmin):
    list_display = ('skill', 'move_up_down_links')

class InterestPostOrderedAdmin(OrderedModelAdmin):
    list_display = ('interest', 'move_up_down_links')

class ProjectPostOrderedAdmin(OrderedModelAdmin):
    list_display = ('title', 'move_up_down_links')

# Register your models here.
admin.site.register(CvPdf)
admin.site.register(Bio)
admin.site.register(EducationPost, CVPostOrderedAdmin)
admin.site.register(WorkPost, CVPostOrderedAdmin)
admin.site.register(ProfessionalEngagementsPost, CVPostOrderedAdmin)
admin.site.register(WorkProjectPost, CVPostOrderedAdmin)
admin.site.register(AchievementPost, CVPostOrderedAdmin)
admin.site.register(QualificationPost, CVPostOrderedAdmin)
admin.site.register(SkillPost, SkillPostOrderedAdmin)
admin.site.register(InterestPost, InterestPostOrderedAdmin)
admin.site.register(ProjectPost, ProjectPostOrderedAdmin)