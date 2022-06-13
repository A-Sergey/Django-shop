from django.urls import reverse_lazy, reverse
from django.views import generic
from django import forms
from .models import CustomUser
from products.models import Product
from django.db.models import Q 
from django.shortcuts import redirect, render
from django.contrib.auth.views import LoginView as Login
from django.contrib import auth
from .forms import RegisterForm, ProfileForm

class RegisterView(generic.CreateView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
        
    def get_success_url(self):
        return reverse('news')
        
    def get_context_data(self, **kwargs):
        if 'reg' not in kwargs:
            kwargs['reg'] = self.get_form()
        return super().get_context_data(**kwargs)


class LoginView(Login):
    def get_success_url(self):
        return reverse('news')

def profile(request):
    user = CustomUser.objects.get(username=auth.get_user(request))
    products_sale = Product.objects.filter(~Q(sell = "")&Q(product_of_the_day=False))
    try:
        product_of_the_day = Product.objects.get(product_of_the_day=True)
    except:
        product_of_the_day = None
    if request.method == 'POST':
        user_form = ProfileForm(request.POST)
        if user_form.is_valid():
            cd = user_form.cleaned_data
            if cd.get("email") != '':
                user.email = cd.get("email")
            if cd.get("date_of_birth") != None:
                user.date_of_birth = cd.get("date_of_birth")
            user.save()
            return redirect(request.META['HTTP_REFERER'])
    else:
        user_form = ProfileForm()
        user_form.fields['email'].widget = forms.TextInput(attrs={'placeholder':user.email})
        user_form.fields['date_of_birth'].widget = forms.TextInput(attrs={'placeholder':user.date_of_birth})

    return render(request, 'registration/profile.html', {'user': user,
                                                         'user_form': user_form,
                                                        },)
    