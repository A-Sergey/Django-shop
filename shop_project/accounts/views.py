from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.urls import reverse_lazy, reverse
from django.views import generic
from django import forms
from .models import CustomUser
from products.models import Product
from django.db.models import Q 
from django.contrib.auth.views import PasswordResetView as PasswordReset
from django.contrib.auth.views import PasswordResetDoneView as PasswordResetDone
from django.contrib.auth.views import PasswordResetConfirmView as PasswordResetConfirm
from django.contrib.auth.views import PasswordResetCompleteView as PasswordResetComplete
from django.contrib.auth.views import LoginView as Login

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
        try:
            product_of_the_day = Product.objects.get(product_of_the_day=True)
        except:
            product_of_the_day = None
        products_sale = Product.objects.filter(~Q(sell = "")&Q(product_of_the_day=False))
        if 'reg' not in kwargs:
            kwargs['reg'] = self.get_form()
        kwargs['product_of_the_day'] = product_of_the_day
        kwargs['products_sale'] = products_sale
        return super().get_context_data(**kwargs)
        
    def get_success_url(self):
        return reverse('news')

class PasswordResetView(PasswordReset):
    def get_context_data(self, **kwargs):
        try:
            product_of_the_day = Product.objects.get(product_of_the_day=True)
        except:
            product_of_the_day = None
        products_sale = Product.objects.filter(~Q(sell = "")&Q(product_of_the_day=False))
        if 'reg' not in kwargs:
            kwargs['reg'] = self.get_form()
        kwargs['product_of_the_day'] = product_of_the_day
        kwargs['products_sale'] = products_sale
        return super().get_context_data(**kwargs)
        
class PasswordResetDoneView(PasswordResetDone):
    def get_context_data(self, **kwargs):
        try:
            product_of_the_day = Product.objects.get(product_of_the_day=True)
        except:
            product_of_the_day = None
        products_sale = Product.objects.filter(~Q(sell = "")&Q(product_of_the_day=False))
        kwargs['product_of_the_day'] = product_of_the_day
        kwargs['products_sale'] = products_sale
        return super().get_context_data(**kwargs)

class PasswordResetConfirmView(PasswordResetConfirm):
    def get_context_data(self, **kwargs):
        try:
            product_of_the_day = Product.objects.get(product_of_the_day=True)
        except:
            product_of_the_day = None
        products_sale = Product.objects.filter(~Q(sell = "")&Q(product_of_the_day=False))
        kwargs['product_of_the_day'] = product_of_the_day
        kwargs['products_sale'] = products_sale
        return super().get_context_data(**kwargs)

class PasswordResetCompleteView(PasswordResetComplete):
    def get_context_data(self, **kwargs):
        try:
            product_of_the_day = Product.objects.get(product_of_the_day=True)
        except:
            product_of_the_day = None
        products_sale = Product.objects.filter(~Q(sell = "")&Q(product_of_the_day=False))
        kwargs['product_of_the_day'] = product_of_the_day
        kwargs['products_sale'] = products_sale
        return super().get_context_data(**kwargs)

class LoginView(Login):
    def get_context_data(self, **kwargs):
        try:
            product_of_the_day = Product.objects.get(product_of_the_day=True)
        except:
            product_of_the_day = None
        products_sale = Product.objects.filter(~Q(sell = "")&Q(product_of_the_day=False))
        kwargs['product_of_the_day'] = product_of_the_day
        kwargs['products_sale'] = products_sale
        return super().get_context_data(**kwargs)
    
    def get_success_url(self):
        return reverse('news')