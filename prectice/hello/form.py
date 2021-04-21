from django import forms
from .models import tebal

class form1(forms.ModelForm):
    class Meta:
        model=tebal
        fields = "__all__"