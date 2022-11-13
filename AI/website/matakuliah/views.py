from django.shortcuts import render

# Create your views here.

from . models import mk

def index(request) :

    post = mk.objects.all()

    context = {
        'tampung' : post,
    }

    return render(request, 'matakuliah/index.html', context)