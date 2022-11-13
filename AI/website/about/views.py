from django.shortcuts import render

# Create your views here.

def index(reqquest) :
    return render(reqquest, 'about/index.html')