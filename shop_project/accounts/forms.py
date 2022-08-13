from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.utils.translation import gettext as _
from django import forms
from .models import CustomUser


class RegisterForm(UserCreationForm):
    email = forms.EmailField(label="Email")
    date_of_birth = forms.DateField(
        label="Date of birth",
        error_messages = {
            "invalid": "Не верно введена дата (дд-мм-гггг)",
        }
    )

    class Meta:
        model = CustomUser
        fields = ("username", "email", "date_of_birth")

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        user.date_of_birth = self.cleaned_data["date_of_birth"]
        if commit:
            user.save()
        return user

    def clean_username(self):
        super(RegisterForm, self).clean()
        username = self.cleaned_data["username"]
        if CustomUser.objects.filter(username = username).exists():
            raise forms.ValidationError("Имя пользователя занято")
        return username

    def clean_email(self):
        super(RegisterForm, self).clean()
        email = self.cleaned_data["email"]
        if CustomUser.objects.filter(email = email).exists():
            raise forms.ValidationError(
                "Адрес электронной почты уже существует")
        return email

class ProfileForm(forms.Form):
    email = forms.EmailField(label=_("Email"), required=False)
    date_of_birth = forms.DateField(
        label=("День рождения"),
        required=False,
    )


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = (
            "username",
            "email",
            "date_of_birth",
        )


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = (
            "username",
            "email",
            "date_of_birth",
        )
