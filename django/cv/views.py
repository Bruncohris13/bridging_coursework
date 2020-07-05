from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from .forms import *
from .models import *

# Create your views here.
def home_page(request):
    quote = Quote.objects.all()
    education = EducationPost.objects.all()
    work = WorkPost.objects.all()
    achievements = AchievementPost.objects.all()
    qualifications = QualificationPost.objects.all()
    skills = SkillPost.objects.all()
    interests = InterestPost.objects.all()
    add_activities = AddActivitiesPost.objects.all()
    projects = ProjectPost.objects.all()
    cv_pdf = CvPdf.objects.all()

    return render(request, 'cv/home_page.html', {
        'quote': quote,
        'education': education,
        'work': work,
        'achievements': achievements,
        'qualifications': qualifications,
        'skills': skills,
        'interests': interests,
        'projects': projects,
        'cv_pdf': cv_pdf,
        'add_activities': add_activities,
    })

@staff_member_required
def quote_edit(request):
    quote = Quote.objects.first()
    if request.method == 'POST':
        form = QuoteForm(request.POST, instance=quote)
        if form.is_valid():
            quote = form.save(commit=False)
            quote.save()
            return redirect('home_page')
    else:
        form = QuoteForm(instance=quote)
    return render(request, 'cv/cv_post_edit.html', {
        'form': form
    })

@staff_member_required
def cv_post_edit(request, category, pk):
    form_class = get_form_class(category)
    post = get_object_or_404(get_post_class(category), pk=pk)
    if request.method == "POST":
        form = form_class(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('home_page')
    else:
        form = form_class(instance=post)
    return render(request, 'cv/cv_post_edit.html', {'form': form})

@staff_member_required
def cv_post_new(request, category):
    form_class = get_form_class(category)
    if request.method == "POST":
        form = form_class(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('home_page')
    else:
        form = form_class()
    return render(request, 'cv/cv_post_edit.html', {'form': form})

@staff_member_required
def cv_post_delete(request, category, pk):
    post = get_object_or_404(get_post_class(category), pk=pk)
    if request.method == "GET":
        if (category == "Project"):
            post.removeImage()
        post.delete()
    return redirect('home_page')

def get_form_class(category):
    switcher = {
        'Education' : EducationPostForm,
        'Work' : WorkPostForm,
        'Achievement' : AchievementPostForm,
        'Qualification' : QualificationPostForm,
        'Skill' : SkillPostForm,
        'Interest' : InterestPostForm,
        'Project' : ProjectPostForm,
        'Add_Activities' : AddActivitiesPostForm,
    }
    return switcher.get(category, "Invalid category")

def get_post_class(category):
    switcher = {
        'Education' : EducationPost,
        'Work' : WorkPost,
        'Achievement' : AchievementPost,
        'Qualification' : QualificationPost,
        'Skill' : SkillPost,
        'Interest' : InterestPost,
        'Project' : ProjectPost,
        'Add_Activities' : AddActivitiesPost,
    }
    return switcher.get(category, "Invalid category")

@staff_member_required
def cv_pdf_upload(request):
    cv_pdf = CvPdf.objects.first()
    if request.method == 'POST':
        form = CvPdfForm(request.POST, request.FILES, instance=cv_pdf)
        if form.is_valid():
            cv_pdf = form.save(commit=False)
            cv_pdf.save()
            return redirect('home_page')
    else:
        form = CvPdfForm(instance=cv_pdf)
    return render(request, 'cv/cv_post_edit.html', {
        'form': form
    })