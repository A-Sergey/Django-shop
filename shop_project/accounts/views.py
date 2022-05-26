from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.urls import reverse_lazy, reverse
from django.views import generic
from django import forms
from .models import CustomUser

class RegisterForm(UserCreationForm):
    email = forms.EmailField(label='Email')
    date_of_birth = forms.DateField(label='Date of birth',widget=forms.DateInput(format='%d/%m%Y'))
    
    class Meta:
        model = CustomUser
        fields = ("username",'email','date_of_birth')
        
    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        user.date_of_birth = self.cleaned_data["date_of_birth"]
        if commit:
            user.save()
        return user


class RegisterView(generic.CreateView):

    form_class = RegisterForm
    template_name = 'registration/register.html'
    def get_context_data(self, **kwargs):
        if 'reg' not in kwargs:
            kwargs['reg'] = self.get_form()
        return super().get_context_data(**kwargs)
        
    def get_success_url(self):
        return reverse('news')