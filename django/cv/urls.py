from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('bio_edit/', views.bio_edit, name='bio_edit'),
    path('cv_post_new/<str:category>/', views.cv_post_new, name='cv_post_new'),
    path('cv_post_edit/<str:category>/<int:pk>/', views.cv_post_edit, name='cv_post_edit'),
    path('cv_post_delete/<str:category>/<int:pk>/', views.cv_post_delete, name='cv_post_delete'),
]