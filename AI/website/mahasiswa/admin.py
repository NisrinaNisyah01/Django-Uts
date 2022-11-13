from django.contrib import admin

# Register your models here.

from . models import mhs

class tampil(admin.ModelAdmin) : 
    list_display = ('nim','nama')
    list_display_links = (None)
    search_fields = ('nim','nama')

admin.site.register(mhs, tampil)