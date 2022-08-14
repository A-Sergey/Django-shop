from django.urls import reverse
from django.views import generic
from django import forms
from django.shortcuts import redirect, render
from django.contrib import auth

from .forms import RegisterForm, ProfileForm
from .models import CustomUser


class RegisterView(generic.CreateView):
    form_class = RegisterForm
    template_name = "registration/register.html"

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("/")
        return super().get(request, *args, **kwargs)

    def get_success_url(self):
        return reverse("news")

    def get_context_data(self, **kwargs):
        if "reg" not in kwargs:
            kwargs["reg"] = self.get_form()
        return super().get_context_data(**kwargs)


def profile(request):
    if not request.user.is_authenticated:
        return redirect("/")
    user = CustomUser.objects.get(username=auth.get_user(request))
    if request.method == "POST":
        user_form = ProfileForm(request.POST)
        if user_form.is_valid():
            cd = user_form.cleaned_data
            if cd.get("email") != "":
                user.email = cd.get("email")
            if cd.get("date_of_birth") != None:
                user.date_of_birth = cd.get("date_of_birth")
            user.save()
            return redirect(request.META["HTTP_REFERER"])
    else:
        user_form = ProfileForm()
        user_form.fields["email"].widget = forms.TextInput(
            attrs={"placeholder": user.email}
        )
        user_form.fields["date_of_birth"].widget = forms.TextInput(
            attrs={"placeholder": user.date_of_birth}
        )
    return render(
        request,
        "registration/profile.html",
        {"user": user, "user_form": user_form},
    )
