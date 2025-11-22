from django import forms

from .models import Topic, Entry

class TopicsForms(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ["text"]
        labels = {"text":""}

class EntryForms(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ["text"]
        labels = {"text":""}
        widget = {"text":forms.Textarea(attrs={'col':80})}
        
        


