from django.shortcuts import render, redirect, get_object_or_404
from .forms import BioForm
from .models import Bio

# Create your views here.
def bio_edit(request):
    if request.method == 'POST':
        form = BioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home_page')
    else:
        form = BioForm()
    return render(request, 'cv/bio_edit.html', {
        'form': form
    })

def home_page(request):
    bio = Bio.objects.all()
    return render(request, 'cv/home_page.html', {
        'bio': bio
    })