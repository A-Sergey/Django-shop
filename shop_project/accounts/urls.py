from django.urls import path
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordChangeView,
    PasswordChangeDoneView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
)
from .views import RegisterView, profile

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path(
        "login/",
        LoginView.as_view(redirect_authenticated_user=True),
        name="login"
    ),
    path("logout/", LogoutView.as_view(), name="logout"),
    path(
        "password_change/",
        PasswordChangeView.as_view(),
        name="password_change"
    ),
    path(
        "password_change/done/",
        PasswordChangeDoneView.as_view(),
        name="password_change_done",
    ),
    path("password_reset/", PasswordResetView.as_view(), name="password_reset"),
    path(
        "password_reset/done/",
        PasswordResetDoneView.as_view(),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        PasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path(
        "reset/done/",
        PasswordResetCompleteView.as_view(),
        name="password_reset_complete",
    ),
    path("profile/", profile, name="profile"),
]
