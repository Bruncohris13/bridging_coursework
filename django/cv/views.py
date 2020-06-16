from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from .models import *

# Create your views here.
def home_page(request):
    bio = Bio.objects.all()
    education = EducationPost.objects.all()
    return render(request, 'cv/home_page.html', {
        'bio': bio,
        'education': education
    })

def bio_edit(request):
    bio = Bio.objects.first()
    if request.method == 'POST':
        form = BioForm(request.POST, request.FILES, instance=bio)
        if form.is_valid():
            bio = form.save(commit=False)
            bio.save()
            return redirect('home_page')
    else:
        form = BioForm(instance=bio)
    return render(request, 'cv/bio_edit.html', {
        'form': form
    })

def cv_post_edit(request, category, pk):
    form_class = get_category(category)
    post = get_object_or_404(EducationPost, pk=pk)
    if request.method == "POST":
        form = form_class(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('home_page')
    else:
        form = form_class(instance=post)
    return render(request, 'cv/cv_post_edit.html', {'form': form})

def cv_post_new(request, category):
    form_class = get_category(category)
    if request.method == "POST":
        form = form_class(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('home_page')
    else:
        form = form_class()
    return render(request, 'cv/cv_post_edit.html', {'form': form})

def get_category(category):
    switcher = {
        'Education' : EducationPostForm
    }
    return switcher.get(category, "Invalid category")