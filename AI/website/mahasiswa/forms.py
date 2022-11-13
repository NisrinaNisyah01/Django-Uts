from django import forms

class tamu(forms.Form) : 
    nim = forms.CharField(max_length=10)
    nama = forms.CharField(max_length=50)