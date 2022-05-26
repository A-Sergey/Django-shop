from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import CustomUser
from shop import settings

class CustomUserCreationForm(UserCreationForm):
    #date_of_birth = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS)
    class Meta:
        model = CustomUser
        fields = ('username','email','date_of_birth',)

class CustomUserChangeForm(UserChangeForm):
    #date_of_birth = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS)
    class Meta:
        model = CustomUser
        fields = ('username','email','date_of_birth',)