from django.shortcuts import render

# Create your views here.
def home_page(request):
    return render(request, 'cv/home_page.html', {})