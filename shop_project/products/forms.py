from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

class FindProduct(forms.Form):
    find_product = forms.CharField(label="Поиск",widget=forms.TextInput(attrs={'placeholder': 'Search'}))