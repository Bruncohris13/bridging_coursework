from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('bio_edit/', views.bio_edit, name='bio_edit'),
    path('cv_post_edit/', views.cv_post_edit, name='cv_post_edit'),
]