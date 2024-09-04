from django.shortcuts import render

from base.models import University

# Create your views here.
def home(request):
    return render(request, "index.html")