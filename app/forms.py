from django import forms
from .models import *

class ExampleForm(forms.ModelForm):
    class Meta:
        model = ExampleModel
        fields = '__all__' 