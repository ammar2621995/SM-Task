from dataclasses import fields
from .models import Document,Protein,Comment,Notification
from django import forms

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = '__all__'


class ProteinForm(forms.ModelForm):
    class Meta:
        model = Protein
        fields = '__all__'

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'

    
class NotificationForm(forms.ModelForm):
    class Meta:
        model = Notification
        fields = '__all__'
