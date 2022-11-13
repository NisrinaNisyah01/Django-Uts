from django.db import models

# Create your models here.

class mhs(models.Model) :
    nim = models.CharField(max_length=10)
    nama = models.CharField(max_length=30)

    def __str__(self) :
        return self.nim