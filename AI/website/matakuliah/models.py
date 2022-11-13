from django.db import models

# Create your models here.

class kategori(models.Model) :
    kategori = models.CharField(max_length=30)

    def __str__(self) :
        return self.kategori

class mk(models.Model) :
    mk = models.CharField(max_length=50)
    definisi = models.TextField()
    dosen = models.CharField(max_length=40)
    kategori = models.ForeignKey(kategori, on_delete=models.SET_NULL, null=True)

    def __str__(self) :
        return self.mk