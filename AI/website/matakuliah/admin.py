from django.contrib import admin

# Register your models here.

from . models import mk, kategori

class tampilkan(admin.ModelAdmin) : 
    list_display = ('mk','kategori')
    list_display_links = (None)

admin.site.register(mk, tampilkan)
admin.site.register(kategori)