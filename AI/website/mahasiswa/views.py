from django.shortcuts import render

# Create your views here.

from . forms import tamu
from . models import mhs

def index(request) :

    buku_tamu = tamu()

    context = {
        'tamu' : buku_tamu
    }

    if request.method == "POST" :
        mhs.objects.create(
            nim = request.POST.get('nim'),
            nama = request.POST.get('nama'),
        )

    return render(request, 'mahasiswa/index.html', context)