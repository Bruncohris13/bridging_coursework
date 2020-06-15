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

def cv_post_edit(request):
    None