from django import forms
from .models import Mysee

class Myform(forms.ModelForm):
    class Meta:
        model = Mysee
        fields = '__all__'