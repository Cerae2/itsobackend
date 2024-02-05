# forms.py

from django import forms
from .models import FileUploads

class YourModelForm(forms.ModelForm):
    files = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

    class Meta:
        model = FileUploads
        fields = '__all__'
