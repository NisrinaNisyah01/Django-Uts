from django.db import models

class Guest(models.Model):
    nim = models.CharField(max_length=10)
    nama = models.CharField(max_length=50)
    kegiatan = models.TextField()

    def _str_(self):
        return self.nim
