from django import forms
from .models import Thema, SubThema

class FormThema(forms.ModelForm):
        class Meta:
            model = Thema
            fields = ["thema"]
            labels = {"thema":""}

class FormSubThema(forms.ModelForm):
      class Meta:
            model = SubThema
            fields = ["subthema"]
            labels = {"subthema":""}