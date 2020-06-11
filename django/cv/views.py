from django.shortcuts import render, redirect, get_object_or_404
from .forms import BioForm

# Create your views here.
def home_page(request):
    if request.method == 'POST':
        form = BioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home_page')
    else:
        form = BioForm()
    return render(request, 'cv/home_page.html', {
        'form': form
    })