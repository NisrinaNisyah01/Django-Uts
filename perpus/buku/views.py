from django.shortcuts import render

from . models import Post

def index(request):
    #! Queryset
    postingan = Post.objects.all()
    contex = {'TampungPostingan' : postingan}
    return render(request, 'buku/index.html',contex)
